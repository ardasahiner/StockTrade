var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');

// Adding methods for POST Request handling
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// Module morgan logs all activity to console
app.use(morgan('dev'));

// Connect to online mongodb Database
var mongoose = require('mongoose');
var connectionuri = require('./db_connect')();
mongoose.connect(connectionuri);

// Send index.html file to browser as frontpage
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

// Route Handler file handles all routing tasks
require('./app/routes/route_handler')(app, express);

app.listen(5000);
console.log('Visit page at localhost:5000!');
