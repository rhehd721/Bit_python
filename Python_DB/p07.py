import sqlite3

from libs.db.dba import getConn

def update_1(n_name, o_name):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update test set name=? where name=?'
    cur.execute(upt_sql,(n_name, o_name))

    conn.commit()
    conn.close()

def delete_1(del_name):
    conn = getConn()
    cur = conn.cursor()
    del_sql = 'delete from test where kor<=?'
    cur.execute(del_sql,(del_name,))

    conn.commit()
    conn.close()


if __name__=="__main__":
    update_1("케냐",'커피')
    delete_1(80)