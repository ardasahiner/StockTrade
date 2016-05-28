// API Router
// API Router will communicate user imformation with the front end
module.exports = function(app) {
  var express = require('express');
  var apiRouter = express.Router();

  // Log function calls to console
  apiRouter.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
  });

  apiRouter.get('/', function(req, res) {
    res.send('API Dashboard');
  });

  return apiRouter;
}
