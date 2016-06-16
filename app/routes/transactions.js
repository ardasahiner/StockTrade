var Transaction = require('../models/transaction')

module.exports = function(app, express, User, jwt, Transaction, userRouter) {

  var transactionRouter = express.Router();

  // @KUNAL: do i need to authenticate again or is this unnecessary? @ARDA It should be there :)
  transactionRouter.use(function(req, res, next) {
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

  transactionRouter.route('/')

   // Gets info for all transactions (admin access only)
  .get(function(req, res) {
    if (req.decoded._doc.admin) {
      Transaction.find(function(err, transactions) {
        if (err) res.send(err);
        res.json(transactions);
      });
    } else {
      res.json({ success : false, message : "You do not have admin access" });
    }
  });

  transactionRouter.route('/:query_username')

  // Gets info for a given user's transactions
  .get(function(req, res) {
    // Verify that user is either admin or user to be requested
    if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
      User.findOne({ username: req.params.query_username }, function(err, user) {
        if (err) res.send(err);

        //find list of transactions associated with this user
        Transaction.findOne({userId: user._id}, function(err, transaction) {
          if(err) res.send(err);
          res.json(transaction.transactionList);
        });
      });
    } else {
      res.json({ success : false, message : "You do not have access to this page." });
    }
  });


  userRouter.use('/transactions', transactionRouter);
}
