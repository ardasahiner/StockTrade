// User Router will handle creating, deleting and accessing user data
module.exports = function(app, express, User, jwt) {
  var userRouter = express.Router();

  userRouter.route('/')
  // Handle new User POST request - creates new User
  .post(function(req, res) {
    var user = new User();

    user.name = req.body.name;
    user.username = req.body.username;
    user.password = req.body.password;
    user.email = req.body.email;
    user.admin = req.body.admin

    user.save(function(err) {
      if (err) res.send(err);
      res.json({ message : 'User created! Welcome ' + user.name + '!' });
    });
  })

  // Verify Token and perform authenticated check
  userRouter.use(function(req, res, next) {

    var token = req.body.token || req.query.token || req.headers['x-access-token'];
    if (token) {

      jwt.verify(token, app.get('secretKey'), function(err, decoded) {
        if (err) {
          return res.json({ success : false, message: 'Failed to authenticate token.' });
        } else {
          req.decoded = decoded;
          req.admin = decoded._doc.admin;

          next();
        }
      });
    } else {
      // No token given
      return res.status(403).send({
        success: false,
        message: 'No token provided.'
      });
    }
  });



  // Handle users GET request - returns all users - requires Admin user
  userRouter.route('/')
  .get(function(req, res) {

    if (req.decoded._doc.admin) {
      User.find(function(err, users) {
        if (err) res.send(err);
        res.json(users);
      });
    } else {
      res.json({ success : false, message : "You do not have admin access" });
    }

  });



  userRouter.route('/:user_id')
  // GET user data - gather user data for specific user_id
  .get(function(req, res) {

    // Break if user is not admin or user under question
    if (req.decoded._doc.admin || req.decoded._doc._id == req.params.user_id) {
      User.findById(req.params.user_id, function(err, user) {
        if (err) res.send(err);
        res.json(user);
      });
    } else {
      res.json({ success : false, message : "You do not have access to this page" });
    }
  })
  // PUT user data - change user data for specific user_id
  .put(function(req, res) {

    // Break if user is not admin or user under question
    if (req.decoded._doc.admin || req.decoded._doc._id == req.params.user_id) {
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
    } else {
      res.json({ success : false, message : "You do not have access to this page" });
    }
  })


  // DELETE user - delete user for specific user_id
  .delete(function(req, res) {

    // Break if user is not admin or user under question
    if (req.decoded._doc.admin || req.decoded._doc._id == req.params.user_id) {
      User.remove({
        _id : req.params.user_id
      }, function(err, user) {
        if (err) res.send(err);
        res.json({ message : 'Successfully deleted' });
      });
    } else {
      res.json({ success : false, message : "You do not have access to this page" });
    }
  });

  app.use('/users', userRouter);
}
