// Using Express to Handle Routing
var express = require('express');
var app = express();

// Configure index.html file
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

// Admin Routers
// TODO: handle user auth and admin access
var adminRouter = express.Router();

adminRouter.get('/', function(req, res) {
  res.send('I am the dashboard!');
});

adminRouter.get('/users', function(req, res) {
  res.send('I show all the users!');
});

adminRouter.get('/data', function(req, res) {
  res.send('I show all the data!');
});

app.use('/admin', adminRouter);

app.listen(3000);
console.log('Visit page at localhost:3000');
