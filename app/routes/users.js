// User Router will handle creating, deleting and accessing user data
module.exports = function(app, express, User, jwt) {
  var userRouter = express.Router();

  // POST request to '/' route does not require authentication,
  // should be allowed to create users without being logged in.
  userRouter.route('/')
  // Handle new User POST request - creates new User
  .post(function(req, res) {

    var user = new User();

    user.firstName = req.body.firstName;
    user.lastName = req.body.lastName;
    user.username = req.body.username;
    user.password = req.body.password;
    user.email = req.body.email;

    //@TODO: ensure password strength and email validity (might also do this in the user model)

    user.save(function(err) {
      if (err) res.send(err);
      res.json({ message : 'User created! Welcome ' + user.username + '!', success: true });
    });
  });


  // Verify Token and perform authenticated check
  userRouter.use(function(req, res, next) {

    var token = req.body.token || req.query.token || req.headers['x-access-token'];

    if (token) {
      jwt.verify(token, app.get('secretKey'), function(err, decoded) {
        if (err) {
          return res.json({ success : false, message: 'Failed to authenticate token.' });
        } else {
          // Decoded token saved into request parameters
          req.decoded = decoded;
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
    // Verify that user is admin
    if (req.decoded._doc.admin) {
      User.find(function(err, users) {
        if (err) res.send(err);
        res.json(users);
      });
    } else {
      res.json({ success : false, message : "You do not have admin access" });
    }

  });



  userRouter.route('/:query_username')
  // GET user data - gather user data for specific username
  .get(function(req, res) {
    // Verify that user is either admin or user to be requested
    if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
      User.findOne({ username: req.params.query_username }, function(err, user) {
        if (err) res.send(err);
        res.json(user);
      });
    } else {
      res.json({ success : false, message : "You do not have access to this page." });
    }
  })

  // PUT user data - change user data for specific username
  .put(function(req, res) {

    // Break if user is not admin or user under question
    if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
      User.findOne({ username: req.params.query_username }, function(err, user) {
        if (err) res.send(err);

        // Commented these fields out becuase you should not be allowed to change these fields.
        // if (req.body.name) user.name = req.body.name;
        // if (req.body.username) user.username = req.body.username;
        // if (req.body.email) user.email = req.body.email;
        if (req.body.password) user.password = req.body.password;
        if (req.body.botAccount) user.botAccount = req.body.botAccount;

        // Shouldn't be able to change whether you're an admin either
        // if (req.decoded._doc.admin && req.body.admin) {
        //   user.admin = req.body.admin;
        // }

        user.save(function(err) {
          if (err) res.send(err);
          res.json({ message : 'User updated!' });
        });

      });
    } else {
      res.json({ success : false, message : "You cannot change this user's information" });
    }
  })


  // DELETE user - delete user for specific username
  .delete(function(req, res) {

    // Break if user is not admin or user under question
    if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
      User.remove({ username: req.params.query_username }, function(err, user) {
        if (err) res.send(err);
        res.json({ message : 'User ' + req.params.query_username + ' successfully deleted' });
      });
    } else {
      res.json({ success : false, message : "You do not have access to this page" });
    }
  });

  app.use('/users', userRouter);
}
