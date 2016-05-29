// API Router will communicate user information with the front end
module.exports = function(app, express) {
  var apiRouter = express.Router();

  // Log function calls to console, useful for dev work and debugging
  // Remove for production
  apiRouter.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
  });

  // Access API dashboard
  apiRouter.get('/', function(req, res) {
    res.send('API Dashboard');
  });

  // Address special case where user is kunal or arda, useful syntax for user verification
  apiRouter.param('username', function(req, res, next, username) {
    if (username == "kunal" || username == "arda") {
      console.log("WELCOME " + username.toUpperCase() + "!");
    }
    req.username = username;
    next();
  })

  app.use('/api', apiRouter);
}
