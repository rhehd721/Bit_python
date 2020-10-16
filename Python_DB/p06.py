import sqlite3

from libs.db.dba import getConn

# def select_1():
#     conn = getConn()
#     cur = conn.cursor()
#     cur.execute('select * from test')
#     rs = cur.fetchall() #받아오기
#     for i in rs:
#         print(i)

def select_2(name):
    conn = getConn()
    cur = conn.cursor()
    cur.execute('select * from test where name=?',(name,))
    rs = cur.fetchmany(1)  # 받아올거다 한개만
    for i in rs:
        print(i)

    conn.close()

if __name__=="__main__":
    fname = input("name : ")
    select_2(fname)


