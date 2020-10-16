from libs.db.mdba import getConn

# conn = getConn()
# print(conn)


# def create_table():
#     conn = getConn()
#     cur = conn.cursor()
#     cur.execute('''
#         create table sj(
#         name varchar(20),
#         kor int,
#         eng int,
#         mat int)
#     ''') #table을 만들건데 이름은 sj야 속에 들어가는 내용은 ()속에 있어
#     conn.commit()
#     conn.close()
#
# def insert_a():
#     conn = getConn()
#     cur = conn.cursor()
#     ins_query = 'insert into sj values(%s,%s,%s,%s)' # 삽입될 내용의 형식은 이런것들이야
#     cur.execute(ins_query, ('홀길동', 70,80,70)) # 삽입될 내용은 이것들이야
#     conn.commit()
#     conn.close()

# def select_a():
#     conn = getConn()
#     cur = conn.cursor()
#     # js = 'select * from sj'  # DB(sj)안에 내용을 가져올것이다
#     js = 'select * from sj where name like %s'
#     cur.execute(js, ('홀길동',))
#     # cur.execute(js)
#     rs = cur.fetchall()
#     print(rs)
#     conn.close()

def display():
    conn = getConn()
    cur = conn.cursor()
    js = 'select * from sj ' # sj 에서 받아온 모든것을 js에 넣어줄거야
    cur.execute(js)
    rs = cur.fetchall()
    for i in range(len(rs)):
        sum = 0
        for j in range(1,3):
            sum += int(rs[i][j])
        print(i,'의 총점 = ',sum)

def update(sco, name):
    conn = getConn()
    cur = conn.cursor()
    upt_sql = 'update sj set kor=%s where name=%s'
    cur.execute(upt_sql, (sco,name,))
    conn.commit()
    conn.close


def delete(name):
    conn = getConn()
    cur = conn.cursor()
    del_sql = 'delete from sj where name=%s'
    cur.execute(del_sql, (name,))
    conn.commit()
    conn.close




if __name__=='__main__':
    # create_table() # 함수들을 실행해줘
    # insert_a()
    # select_a()
    # update('50','홀길동')
    delete('홀길동')
    display()
