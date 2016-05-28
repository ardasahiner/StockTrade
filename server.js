// Using Express to Handle Routing
var express = require('express');
var app = express();

// Configure index.html file
app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

//TODO: Move Routing operations to separate handler
// Import AdminRouter from routers directory
var adminRouter = require('./routes/adminRouter')(app);
app.use('/admin', adminRouter);

//Import APIRouter from routers directory
var apiRouter = require('./routes/apiRouter')(app);
app.use('/api', apiRouter);

app.listen(3000);
console.log('Visit page at localhost:3000');
