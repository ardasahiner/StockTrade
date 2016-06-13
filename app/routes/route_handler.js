module.exports = function(app, express) {
  
  var jwt = require('jsonwebtoken');
  var User = require('../models/user');

  // Calls to admin and api routers, adds themselves to the application
  require('./admin')(app, express, User, jwt);
  require('./api')(app, express, User, jwt);
  require('./authentication')(app, express, User, jwt);
  require('./users')(app, express, User, jwt);
  require('./stock')(app, express, User, jwt);
}
