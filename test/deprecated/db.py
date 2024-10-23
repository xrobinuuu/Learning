import copy
import datetime
import json
import os
import pathlib
import random
import threading
import traceback
import pandas as pd
import psycopg2
from psycopg2 import DatabaseError
from psycopg2.sql import SQL, Identifier
from dbutils.pooled_db import PooledDB


db_local = threading.local()


def retry(func):
    def wrapper(*args, **kwargs):
        res = str()
        for i in range(3):
            res = func(*args, **kwargs)
            if not isinstance(res, str):
                return res
            else:
                DB.check_spl()
        return res
    return wrapper


class DB:

    @staticmethod
    def check_spl(i=0, circle=2, n=None):
        sid = f"{os.getpid()}_{str(threading.current_thread()).split(' ')[-1][:-2]}"
        if hasattr(db_local, sid):
            old_spl = db_local.__dict__.get(sid)
            if isinstance(old_spl, PooledDB):
                old_spl.close()
            db_local.__delattr__(sid)
        config_params = DB.db_config()
        dsn_tmp = config_params.get('DSN')
        dsn = copy.deepcopy(dsn_tmp)
        host_ls = config_params.get('host')
        host_num = len(host_ls)
        if n is None:
            n = circle * host_num
        if n <= 0:
            return None
        dsn.update({'host': host_ls[i]})
        try:
            spl = PooledDB(creator=psycopg2, mincached=1, maxcached=5, blocking=True, **dsn)
            conn = spl.connection()
            mark = DB.check_conn(conn)
            if not isinstance(mark, str):
                db_local.__setattr__(sid, spl)
                DB.fix_hosts(dsn.get("host"))
            else:
                return DB.check_spl(i=(i + 1) % host_num, n=n - 1)
        except DatabaseError:
            return DB.check_spl(i=(i + 1) % host_num, n=n - 1)

    @staticmethod
    def connection(n=2):
        if n < 0:
            return None
        try:
            spl = db_local.__dict__.get(f"{os.getpid()}_{str(threading.current_thread()).split(' ')[-1][:-2]}")
            if spl is None:
                DB.check_spl()
                return DB.connection(n - 1)
            conn = spl.connection()
            return conn
        except DatabaseError:
            DB.check_spl()
            return DB.connection(n - 1)

    @staticmethod
    def check_conn(conn, close=True):
        try:
            check_sql = DB.db_config().get('check_sql')
            if check_sql:
                with conn.cursor() as cs:
                    cs.execute(random.choice(check_sql))
            return True
        except DatabaseError:
            return traceback.format_exc()
        finally:
            if close:
                conn.close()

    @staticmethod
    def db_config():
        config_path = str(pathlib.Path(__file__).resolve().parent.joinpath("config.json").absolute())
        with open(config_path, 'r') as f:
            config_params = json.loads(f.read())
        return config_params

    @staticmethod
    def fix_hosts(host):
        config_path = str(pathlib.Path(__file__).resolve().parent.joinpath("config.json").absolute())
        config_params = DB.db_config()
        hosts = config_params.get("host")
        if hosts[0] != host:
            hosts.remove(host)
            hosts.insert(0, host)
            with open(config_path, 'w') as f:
                f.write(json.dumps(config_params))

    @staticmethod
    def trans_type(data):  # 数据类型转换
        if isinstance(data, str):
            return data.strip()
        elif isinstance(data, memoryview):
            return bytes(data)
        else:
            return data

    @staticmethod
    def trans_data(field: list, ls: list):  # 转换返回数据类型
        result = pd.DataFrame(ls, columns=field)
        return result.applymap(DB.trans_type)

    @staticmethod
    @retry
    def raw_sql(sql, values=()):
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            with conn.cursor() as cs:
                cs.execute(sql, values)
                query_ls = cs.fetchall()
            return query_ls
        except DatabaseError:
            return traceback.format_exc()
        except ValueError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def create(table, intm=True, **kwargs):  # 数据库增加记录
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            keys = list(kwargs.keys())
            values = list(kwargs.values())
            if intm:
                keys.append('intm')
                dt = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                values.append(dt)
            insert_position = '(' + ','.join(["%s"] * len(values)) + ')'
            table_column = '(' + ','.join(keys) + ')'
            sql = SQL("INSERT INTO {} " + f"{table_column}" + " VALUES " + f"{insert_position}").format(Identifier(table))
            with conn.cursor() as cs:
                cs.execute(sql, values)
            conn.commit()
            return True
        except DatabaseError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def filter(table, field=None, **kwargs):  # 数据库查询操作
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            if kwargs:
                values = list(kwargs.values())
                condition = ' AND '.join([key + '=%s' for key in kwargs.keys()])
                if field:
                    fld = ','.join(field)
                    sql = SQL("SELECT " + f"{fld}" + " FROM {} WHERE " + f"{condition}").format(Identifier(table))
                else:
                    sql = SQL("SELECT * FROM {} WHERE " + f"{condition}").format(Identifier(table))
                with conn.cursor() as cs:
                    cs.execute(sql, values)
                    if field:
                        fields = field
                    else:
                        fields = [desc[0] for desc in cs.description]
                    query_ls = cs.fetchall()
                return DB.trans_data(fields, query_ls)
            else:
                if field:
                    fld = ','.join(field)
                    sql = SQL("SELECT " + f"{fld}" + " FROM {}").format(Identifier(table))
                else:
                    sql = SQL("SELECT * FROM {}").format(Identifier(table))
                with conn.cursor() as cs:
                    cs.execute(sql)
                    if field:
                        fields = field
                    else:
                        fields = [desc[0] for desc in cs.description]
                    query_ls = cs.fetchall()
                return DB.trans_data(fields, query_ls)
        except DatabaseError:
            return traceback.format_exc()
        except ValueError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def update(table, replace: dict, condition: dict):  # 数据库更新操作
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            rep = ','.join([key + '=%s' for key in replace.keys()])
            cond = ' AND '.join([key + '=%s' for key in condition.keys()])
            values = list(replace.values())
            values.extend(list(condition.values()))
            sql = SQL("UPDATE {} SET " + f"{rep}" + " WHERE " + f"{cond}").format(Identifier(table))
            with conn.cursor() as cs:
                cs.execute(sql, values)
            conn.commit()
            return True
        except DatabaseError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def delete(table, **kwargs):  # 数据库删除操作
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            if kwargs:
                values = list(kwargs.values())
                condition = ' AND '.join([key + '=%s' for key in kwargs.keys()])
                sql = SQL("DELETE FROM {} WHERE " + f"{condition}").format(Identifier(table))
                with conn.cursor() as cs:
                    cs.execute(sql, values)
                conn.commit()
                return True
            return False
        except DatabaseError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def upsert(table, primary_columns, normal_columns, values):
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            columns = primary_columns + normal_columns
            column_str = '(' + ','.join(list(map(str, columns))) + ')'
            values_str = '(' + ','.join(["%s"] * len(columns)) + ')'
            primary_columns_str = '(' + ','.join(list(map(str, primary_columns))) + ')'
            normal_columns_str = '=%s,'.join(normal_columns) + "=%s"
            sql = SQL("INSERT INTO {}" + f"{column_str} VALUES{values_str} ON CONFLICT {primary_columns_str} DO UPDATE SET {normal_columns_str}").format(Identifier(table))
            with conn.cursor() as cs:
                cs.executemany(sql, values)
            conn.commit()
            return True
        except DatabaseError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def delete_many(table, primary_columns, values):
        if not values:
            return False
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            primary_columns_str = '=%s and '.join(primary_columns) + "=%s"
            sql = SQL("DELETE FROM {} WHERE " + f"{primary_columns_str}").format(Identifier(table))
            with conn.cursor() as cs:
                cs.executemany(sql, values)
            conn.commit()
            return True
        except DatabaseError:
            return traceback.format_exc()
        finally:
            conn.close()

    @staticmethod
    @retry
    def create_many(table, columns, primary_columns, values):
        conn = DB.connection()
        if conn is None:
            return "无可用连接"
        try:
            primary_columns_str = '(' + ','.join(list(map(str, primary_columns))) + ')'
            column_str = '(' + ','.join(list(map(str, columns))) + ')'
            values_str = '(' + ','.join(["%s"] * len(columns)) + ')'
            sql = SQL("INSERT INTO {} " + f"{column_str} VALUES {values_str} ON CONFLICT {primary_columns_str} DO NOTHING").format(Identifier(table))
            with conn.cursor() as cs:
                cs.executemany(sql, values)
            conn.commit()
            return True
        except DatabaseError:
            return traceback.format_exc()
        finally:
            conn.close()