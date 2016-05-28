// Using Express to Handle Routing
var express = require('express');
var app = express();

// Send index.html file to browser
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

// Route Handler file handles all routing
require('./routes/route_handler')(app, express);

app.listen(5000);
console.log('Visit page at localhost:5000!');
