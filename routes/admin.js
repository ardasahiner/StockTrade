// Administrator Router
// Admin Router will communicate administrative information
module.exports = function(app, express) {
  var adminRouter = express.Router();

  // Log function calls to console, useful for dev work and debugging
  adminRouter.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
  });

  adminRouter.get('/', function(req, res) {
    res.send('Admin Dashboard');
  });

  // Access administrative user data - priviledged data access
  adminRouter.get('/users', function(req, res) {
    res.send('User Data');
  });

  app.use('/admin', adminRouter);
}
