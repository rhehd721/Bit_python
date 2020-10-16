# from xml.etree.ElementTree import * # *은 '모든걸 다 가져와!' 라는 뜻
#
# person = Element('person') #<person> </person>
# name = Element('name') #<name> </name>
# name.text = 'honggildong'
# person.append(name)
#
#
# age = Element('age') #<age> </age>
# age.text = '22'
# person.append(age)
#
# SubElement(person, 'address').text = '서울'
#
# dump(person)
#
# ElementTree(person).write('C:/Users/bit/Desktop/새 폴더/person.xml')

# import xml.etree.ElementTree as EE
#
# f = EE.parse('C:/Users/bit/Desktop/새 폴더/person.xml')
# root = f.getroot()
# print(root.tag)
#
# for i in root:
#     print(i.tag, i.text)

# li = [{'name' : '홍길동', 'kok':60, 'eng':80, 'mat':90},
#       {'name' : '이영자', 'kok':30, 'eng':20, 'mat':10},
#       {'name' : '김철수', 'kok':0, 'eng':0, 'mat':10},
#       ]
#
# import json
#
# with open('C:/Users/bit/Desktop/새 폴더/grade.json', 'w') as f:
#     json.dump(li,f,ensure_ascii=False)

# import json
#
# with open('C:/Users/bit/Desktop/새 폴더/grade.json', 'r') as f:
#     data = json.load(f)
#
# for i in data:
#     for k, v in i.items():
#         print(k,v)
#         i_list = list(i(value))
#     print("#"*20)
#     print(i_list)

# from libs.mymath.cal import add
#
# print(add(10,5))

import sqlite3

from libs.db.dba import getConn

def create_table():
    conn = getConn() #DB와 접속 정보
    cur = conn.cursor() #DB를 보는 포인터
    cur.execute('''
        create table test(name text,
        kor int,
        eng int,
        mat int)
    ''')
    conn.commit() # 데이터베이스의 변경사항 확정
    conn.close() #닫아준다

if __name__=='__main__': # 다른 파일에어서 이 함수를 중복으로 사용되지 않게 하기위해??
    create_table()