// Administrator Router
// Admin Router will communicate administrative information with relevant users
module.exports = function(app) {
  var express = require('express');
  var adminRouter = express.Router();

  // Log function calls to console
  adminRouter.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
  });

  adminRouter.get('/', function(req, res) {
    res.send('Admin Dashboard');
  });

  adminRouter.get('/users', function(req, res) {
    res.send('User Data');
  });

  return adminRouter;
}
