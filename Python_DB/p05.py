import sqlite3

from libs.db.dba import getConn

def insert_1():
    conn = getConn()
    cur = conn.cursor()
    cur.execute('''
        insert into test values('홀길동',60,70,80)
    ''')
    conn.commit()
    conn.close()

def insert_2():
    conn = getConn()
    cur = conn.cursor()
    ins_sq1 = 'insert into test values(?,?,?,?)'  # 동적쿼리
    cur.execute(ins_sq1, ('김철수',55,66,77)) #반드시 튜플형태로
    conn.commit()
    conn.close()

def insert_3():
    conn = getConn()
    cur = conn.cursor()
    li = [('이영자',77,88,99),('한의원',78,45,11),('커피',11,22,33)]
    ins_sq1 = 'insert into test values(?,?,?,?)'  # 동적쿼리
    cur.executemany(ins_sq1, li) #리스트 내부구조는 튜플
    cur.execute(ins_sq1, ('김철수',55,66,77)) #반드시 튜플형태로
    conn.commit()
    conn.close()

if __name__=="__main__":
    #print(__name__)
    # insert_1()
    # insert_2()
    insert_3()