const express = require('express');
const fs = require('fs').promises;
const app = express();
var http = require('http').Server(app);
var socketio = require('socket.io')(http);
const port = 3000;
const hostname = 'your ip here';
app.use(express.json());

app.get('/', (req, res) => {
    fs.readFile(__dirname + '/Site.html')
    .then(content => {
        res.setHeader("Content-Type", "text/html");
        res.writeHead(200);
        res.end(content);
    })
})

app.post('/setcoords', (req, res) => {
    data = req.body;
    socketio.emit('receiveData', data)
    console.log(data);
    res.statusCode = 200;
    res.sendStatus(200);
})

app.get('/coords', (req, res) => {
    res.setHeader('Content-Type', 'application/json');
    res.writeHead(200);
    res.end(JSON.stringify(coords));
})

socketio.on('connection', (socket) => {
    console.log('Socket connected');
})

http.listen(port, () => {
    console.log(`Listening in on http://${hostname}:${port}/`);
});
