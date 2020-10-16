import sqlite3

def getConn(dbpath):
    #mydb.db가 있으면 사용, 없으면 새로 만들겠다.
    conn=sqlite3.connect(dbpath)
    return conn

# def getConn():
#     #mydb.db가 있으면 사용, 없으면 새로 만들겠다.
#     conn=sqlite3.connect('C:/Users/bit/Desktop/새 폴더/mydb.db')
#     return conn