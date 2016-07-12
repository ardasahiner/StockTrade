var TransactionList = require('../models/transactionlist');

module.exports = function (app, express, User, jwt, Transaction, userRouter) {

  var transactionRouter = express.Router();

  transactionRouter.use(function (req, res, next) {
    var token = req.body.token || req.query.token || req.headers['x-access-token'];

    if (token) {
      jwt.verify(token, app.get('secretKey'), function (err, decoded) {
        if (err) {
          return res.status(403).json({success: false, message: 'Failed to authenticate token.'});
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
  .get(function (req, res) {
    if (req.decoded._doc.admin) {
      Transaction.find(function (err, transactions) {
        if (err) res.send(err);
        res.status(200).json({success: true, message: "success!", list: transactions});
      });
    } else {
      res.status(404).json({success: false, message: "You do not have admin access"});
    }
  });

  transactionRouter.route('/:query_username')

  // Gets info for a given user's transactions
  .get(function (req, res) {
    // Verify that user is either admin or user to be requested
    if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
      TransactionList.findOne({username: req.params.query_username}, function (err, transactionlist) {
        if (err) res.send(err);
        res.status(200).json({success: true, message: "success!", list: transactionlist.transactions});
      });
    } else {
      res.status(404).json({success: false, message: "You do not have access to this page."});
    }
  });


  userRouter.use('/transactions', transactionRouter);
};
