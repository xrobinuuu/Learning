import multiprocessing
import pathlib
import time
from concurrent.futures import ThreadPoolExecutor


class Oracle2PG:

    def __init__(self, input_path, output_path=None):
        if not input_path.exists():
            raise FileNotFoundError("path not valid")
        if input_path.is_file():
            self.run = self.oracle_sql_file2pg
            self.input_path = input_path
            if output_path is not None and output_path.exists():
                self.output_path = output_path
            else:
                self.output_path = input_path.parent
        else:
            if not output_path.exists():
                output_path.mkdir()
            self.run = self.oracle_sql_dir2pg
            self.input_path = input_path
            self.output_path = output_path

    @staticmethod
    def cap2lower(data):
        data = data[:11] + data[11:].lower()
        return data

    @staticmethod
    def sep2escape(data, mark=b";"):
        i = 0
        esql_mark = 0
        while i < len(data):
            if mark not in data[i:]:
                break
            sep_start_idx = i + data[i:].index(mark)
            data = data[:sep_start_idx][::-1].replace(b"' ,", b"'E ,", 1)[::-1] + data[sep_start_idx:]
            i = sep_start_idx + 2
            esql_mark = 1
        return data, esql_mark

    @staticmethod
    def hex2escape(data):
        while b"HEXTORAW" in data:
            hex_start_idx = data.index(b"HEXTORAW")
            data = data[:hex_start_idx] + data[hex_start_idx:].replace(b")", b"", 1).replace(b"HEXTORAW('", rb"E'\\x", 1)
        return data

    def oracle_sql2pg(self, sql):
        esql_mark = 2
        if b'INSERT INTO' in sql and b"VALUES" in sql:
            top, bottom = sql.split(b"VALUES")
            top = self.cap2lower(top)
            bottom, esql_mark = self.sep2escape(self.hex2escape(bottom))
            sql = b"VALUES".join([top, bottom])
        return sql, esql_mark

    def oracle_sql_file2pg(self, filename=None):
        filename = filename if filename is not None else self.input_path
        with open(filename, "rb") as f:
            oracle_sql_data = f.read()
        oracle_sql_data = oracle_sql_data.replace(b"'''", b"'")
        oracle_sql_ls = oracle_sql_data.split(b";\r\n")
        pool = ThreadPoolExecutor(max_workers=20)
        ft_ls = list()
        for line in oracle_sql_ls:
            ft = pool.submit(self.oracle_sql2pg, line)
            ft_ls.append(ft)
        pg_sql_ls = list()
        pg_esql_ls = list()
        for future in ft_ls:
            pg_sql, esql_mark = future.result()
            if esql_mark == 0:
                pg_sql_ls.append(pg_sql)
            elif esql_mark == 1:
                pg_esql_ls.append(pg_sql)
            else:
                pg_sql_ls.append(pg_sql)
                pg_esql_ls.append(pg_sql)
        pg_sql_data = b";\r\n".join(pg_sql_ls)
        pg_esql_data = b";\r\n".join(pg_esql_ls)
        self.write2file(filename.name.replace(".sql", "_LOWER.sql"), pg_sql_data)
        self.write2file(filename.name.replace(".sql", "_LOWER_E.sql"), pg_esql_data)

    def oracle_sql_dir2pg(self):
        pool = multiprocessing.Pool(processes=10)
        for input_file in self.input_path.rglob("*.sql"):
            pool.apply_async(func=self.oracle_sql_file2pg, args=(input_file, ))
        pool.close()
        pool.join()

    def write2file(self, filename, data):
        with open(self.output_path.joinpath(filename), "wb") as f:
            f.write(data)


if __name__ == '__main__':
    sql_dir = pathlib.Path(__file__).resolve().parent.joinpath("inputs")
    sql_lower_dir = pathlib.Path(__file__).resolve().parent.joinpath("outputs")
    o2p = Oracle2PG(sql_dir, sql_lower_dir)
    t_1 = time.perf_counter()
    o2p.run()
    t_2 = time.perf_counter()
    print(t_2 - t_1)