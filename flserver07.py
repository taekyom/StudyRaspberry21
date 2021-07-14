# index.html 로딩 서버
from flask import Flask, render_template, request
import MySQLdb as mysql

#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') #접속하는 최초 url
def index():
    db = mysql.connect('localhost', 'root', '12345', 'test', charset='utf8') #charset='utf8'을 써야 한글 추출 가능
    cur = db.cursor(mysql.cursors.DictCursor)
    cur.execute('SELECT * FROM student')
    result = []
    while True:
        student = cur.fetchone() #cursor를 하나씩 내려가게 하는 것
        if not student: break
        result.append(student) #리스트 추가

    cur.close()
    db.close()    
    #데이터를 백엔드에서 프론트엔드로 전달 
    return render_template('mysqldata.html', row=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True) #debug=True : 디버깅을 할 수 있는 상태를 만들어줌(없으면 그냥 실행만 가능)    