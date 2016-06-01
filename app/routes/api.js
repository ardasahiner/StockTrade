// API Router will communicate user information with the front end
module.exports = function(app, express) {
  var apiRouter = express.Router();

  //@TODO: consolidate files so that all backend routes are under
  // ./api

  //@TODO: authentication (post)

  //@TODO: middleware to ensure authenticated


  // Access API dashboard
  apiRouter.get('/', function(req, res) {
    res.send('API Dashboard');
  });

  app.use('/api', apiRouter);
}
