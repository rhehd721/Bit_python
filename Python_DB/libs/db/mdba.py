import mysql.connector

config = {
    "user" : 'root',
    'password' : 'sch1005',
    'host' : '127.0.0.1',
    'database' : "pythondb",
    'port': '3306',
} # 실제 나의 DB프로그램의 정보들을 입력

def getConn():
    conn = mysql.connector.connect(**config)
    return conn

# def get_test(**con):
#     print(con)
#
# get_test(a=1,b=2,c=3,d=4)