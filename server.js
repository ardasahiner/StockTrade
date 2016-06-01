var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var morgan = require('morgan');
var mongoose = require('mongoose');
var port = process.env.PORT || 5000;

// Adding methods for POST Request handling
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());

// Module morgan logs all activity to console
app.use(morgan('dev'));

// Connect to online mongodb Database
var connectionuri = require('./db_connect')();
mongoose.connect(connectionuri);

// Inject index.html file as frontpage
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

// Route Handler file handles all routing tasks
require('./app/routes/route_handler')(app, express);

// Example call to the stock scraper, logs stock price for tsla
require('./scrapers/stock_scraper')('tsla', 'll');

app.listen(port);
console.log('Visit page at localhost:' + port);
