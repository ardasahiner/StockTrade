var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');
var mongoose = require('mongoose');
var jwt = require('jsonwebtoken');
var config = require('./config');

var port = process.env.PORT || 5000;
app.set('secretKey', config.key);

// Connect to online mongodb Database
mongoose.connect(config.database);

// Adding methods for POST Request handling
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// Module morgan logs all activity to console
app.use(morgan('dev'));

// Inject index.html file as frontpage
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

// Route Handler file handles all routing tasks
require('./app/routes/route_handler')(app, express);

app.listen(port);
console.log('Visit page at localhost:' + port);
