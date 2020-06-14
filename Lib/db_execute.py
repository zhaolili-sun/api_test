import pyodbc
from Lib.config import *
# 获取连接方法
def get_db_conn():
    conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=40.125.165.3,16878,1433;DATABASE=TELDCMS;UID=sa;PWD=Teld@teld.cn')
    return conn

# 封装数据库查询操作
def query_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)    # 输出执行的sql
    cur.execute(sql)
    result = cur.fetchone()
    logging.debug(result)  # 输出查询结果
    cur.close()
    conn.close()
    return result

# 封装更改数据库操作
def change_db(sql):
    conn = get_db_conn()
    cur = conn.cursor()
    logging.debug(sql)  # 输出执行的sql
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        logging.error(str(e))  # 输出错误信息
    finally:
        cur.close()
        conn.close()


