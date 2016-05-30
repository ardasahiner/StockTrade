// User Router will handle creating, deleting and accessing user data
module.exports = function(app, express) {
  var userRouter = express.Router();

  // Import User Schema
  var User = require('../models/user');

  userRouter.route('/')
  // Handle new User POST request - creates new User
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
  // Handle users GET request - returns all users
  .get(function(req, res) {
    User.find(function(err, users) {
      if (err) res.send(err);
      res.json(users);
    });
  });

  userRouter.route('/:user_id')
  // GET user data - gather user data for specific user_id
  .get(function(req, res) {
    User.findById(req.params.user_id, function(err, user) {
      if (err) res.send(err);
      res.json(user);
    });
  })
  // PUT user data - change user data for specific user_id
  .put(function(req, res) {
    User.findById(req.params.user_id, function(err, user) {
      if (err) res.send(err);

      if (req.body.name) user.name = req.body.name;
      if (req.body.username) user.username = req.body.username;
      if (req.body.password) user.password = req.body.password;

      user.save(function(err) {
        if (err) res.send(err);
        res.json({ message : 'User updated!' });
      });
    });
  })
  // DELETE user - delete user for specific user_id
  .delete(function(req, res) {
    User.remove({
      _id : req.params.user_id
    }, function(err, user) {
      if (err) res.send(err);
      res.json({ message : 'Successfully deleted' });
    });
  });

  app.use('/user', userRouter);
}
