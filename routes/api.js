// API Router
// API Router will communicate user imformation with the front end
module.exports = function(app, express) {
  var apiRouter = express.Router();

  // Log function calls to console, useful for dev work and debugging
  apiRouter.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
  });

  apiRouter.get('/', function(req, res) {
    res.send('API Dashboard');
  });

  // Access aggregate user data
  apiRouter.get('/users', function(req, res) {
    res.send('User Data');
  });

  // Access user parameters
  // This api call will connect to database to pull user's data
  apiRouter.get('/users/:name', function(req, res) {
    res.send('hello ' + req.params.name + '!');
  });

  app.use('/api', apiRouter);
}
