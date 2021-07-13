//javascript Node.js
var http = require('http'); 
http.createServer(function(req, res)
{
    res.writeHead(200, {'Content-Type' : 'text/plain'});
    res.end('Hello NodeJS\n');
}).listen(8080, '127.0.0.1');
console.log('Server is running at http://127.0.0.1:8080'); //node.js가 서버를 실행하는 것