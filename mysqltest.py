import MySQLdb

#순서 : ip/domain, userid, password, database
db = MySQLdb.connect('localhost', 'root', '12345', 'test', charset='utf8') #charset='utf8'을 써야 한글 추출 가능
cur = db.cursor(MySQLdb.cursors.DictCursor) #cursor : 테이블의 데이터를 한줄한줄 내려가면서 가리키는 것

#insert부분
cur.execute("INSERT INTO student values ({0}, '{1}', '{2}')"
        .format(3, 'FullName', '1987-06-24'))

#select 부분
cur.execute('SELECT * FROM student')

while True:
    student = cur.fetchone() #fetchone : cursor를 하나씩 내려가게 하는 것
    if not student: break

    print(student)

cur.close()
db.close()    