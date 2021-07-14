from flask import Flask

app = Flask(__name__)

@app.route('/') #컨트롤러 부분
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        <meta http-equiv='X-UA-Compatible' content='IE=edge'>
        <title>Node.js WebPage</title>
        <meta name='viewport' content='width=device-width, initial-scale=1'>
        <link rel='stylesheet' type='text/css' media='screen' href="{{url_for('static', filename='css/main.css')}}">
        <!--<script src='main.js'></script>-->
    </head>
    <body>
        <h1> Hello Flask </h1>
        <h3> 제목줄입니다 </h3>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)    