var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');
var mongoose = require('mongoose');
var path = require('path');
var config = require('./config');

var port = config.port;
app.set('port', port);
app.set('secretKey', config.key);

// Connect to online mongodb Database
mongoose.connect(config.database);

// Adding methods for POST Request handling
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// Configure app to handle CORS requests
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, content-type, Authorization');
    next();
});

// Module morgan logs all activity to console
app.use(morgan('dev'));

// Configure express to handle public static files
app.use(express.static(__dirname + '/public'));

// Route Handler file handles all routing tasks
require('./app/routes/route_handler')(app, express);

// Create catch all route, and pass all routes not handled in route_handler to Angular frontend
app.get('*', function (req, res) {
    res.sendFile(path.join(__dirname + '/public/app/views/index.html'));
});

//handling errors?
app.use(function(err, req, res, next) {
  res.status(403).send("something broke!");
});

app.listen(port);
module.exports = app;

console.log('Visit page at localhost:' + port);
console.log('vStock Analytics | Copyright (C) 2016');
