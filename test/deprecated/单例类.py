from dbutils.pooled_db import PooledDB
import MySQLdb


class Dl:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, dsn):
        self.pool = PooledDB(**dsn)

    @property
    def connection(self):
        conn = self.pool.connection()
        conn = self.check(conn)
        return conn

    def check(self, con, n=3):
        if n <= 0:
            return con
        try:
            with con.cursor() as cs:
                cs.execute("select * from table")
            return con
        except:
            self.pool.close()
            self.pool = PooledDB(self.dsn)
            conn = self.pool.connection()
            self.check(conn, n - 1)


d = {'creator': MySQLdb,
     'host': "127.0.0.1",
     'user': 'robin',
     'passwd': '123456',
     'port': 3306,
     'db': 'robin'}

DB = Dl(d)