// Authentication Router
// Authentication Router will handle user authentication and token delivery
module.exports = function (app, express, User, jwt) {
  var authRouter = express.Router();

  // POST requests to handle authentication, if successful will return token
  authRouter.post('/', function (req, res) {

    // Find User, if exists
    User.findOne({
      username: req.body.username
    }, function (err, user) {

      if (err) throw err;

      // User does not exist case
      if (!user) {
        res.json({success: false, message: 'Authentication failed. User not found.'});

      } else if (user) {
        // Password does not match case
        if (!user.comparePassword(req.body.password)) {
          res.json({success: false, message: 'Authentication failed. Wrong password.'});

        } else {
          // Create token, authentication passed
          if (req.body.rememberMe) {
            var token = jwt.sign(user, app.get('secretKey'), {
              expiresIn: 60*60*24*365 // expires in one year
            });
          } else {
            var token = jwt.sign(user, app.get('secretKey'), {
              expiresIn: 60*60 // expires in one hour
            });
          }

          // return the information including token as JSON
          res.json({
            success: true,
            message: "You've been authenticated!",
            token: token
          });
        }
      }
    });
  });

  app.use('/authenticate', authRouter);
};
