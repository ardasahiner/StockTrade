var jwt   = require('jsonwebtoken');
var User  = require('../models/user');
var stockDictionary = require('../../vendor/stockdict');

module.exports = function(app, express) {

  // Calls to admin and api routers, adds themselves to the application
  require('./admin')(app, express, User, jwt);
  require('./api')(app, express, User, jwt);
  require('./authentication')(app, express, User, jwt);
  require('./users')(app, express, User, jwt);
  require('./stocks')(app, express, User, jwt, stockDictionary;
}
