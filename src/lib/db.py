import MySQLdb


# 接続する
def getConn(user_name, user_pwd, host, db_name):
    return MySQLdb.connect(
        # mysql.sockのPath
        unix_socket='/tmp/mysql.sock',
        user=user_name,
        passwd=user_pwd,
        host=host,
        db=db_name
    )


def db_close(cur, conn):
    cur.close
    conn.close
