// User Router will handle creating, deleting and accessing user data
module.exports = function(app, express) {
  var userRouter = express.Router();

  // Log function calls to console, useful for dev work and debugging
  // Remove for production
  userRouter.use(function(req, res, next) {
    console.log(req.method, req.url);
    next();
  });

  // Import User Schema
  var User = require('../models/user');

  userRouter.route('/')
    // Handle new User POST request - creates new User instance
    .post(function(req, res) {
      var user = new User();

      user.name = req.body.name;
      user.username = req.body.username;
      user.password = req.body.password;

      user.save(function(err) {
        if (err) res.send(err);
        res.json({ message : 'User created! Welcome ' + user.name + '!' });
      });
    })
    // Handle users GET request - returns all user data
    .get(function(req, res) {
      User.find(function(err, users) {
        if (err) res.send(err);

        res.json(users);
      });
    });

  app.use('/user', userRouter);
}
