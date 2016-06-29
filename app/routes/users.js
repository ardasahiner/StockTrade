var mrtScraper = require('../../scrapers/markitrealtimescraper');
var Portfolio = require('../models/portfolio');

// User Router will handle creating, deleting and accessing user data
module.exports = function (app, express, User, jwt, TransactionList, Transaction, UserAsset) {
    var userRouter = express.Router();

    // POST request to '/' route does not require authentication,
    // should be allowed to create users without being logged in.
    userRouter.route('/')
        // Handle new User POST request - creates new User
        .post(function (req, res) {

            var user = new User();
            //@TODO: ensure password strength and email validity (might also do this in the user model)
            user.firstName = req.body.firstName;
            user.lastName = req.body.lastName;
            user.username = req.body.username;
            user.password = req.body.password;
            user.email = req.body.email;

            // callback hell lmao
            user.save(function (err) {
                  if (err) {
                    res.send(err);
                  } else {

                    var tl = new TransactionList();
                    tl.username = req.body.username;
                    tl.save(function (err) {
                      if (err) {
                        res.send(err);
                      } else {

                        var p = new Portfolio();
                        p.username = req.body.username;
                        p.save(function (err) {
                          if (err) {
                            res.send(err);
                          } else {
                            res.json({message: 'User created! Welcome ' + req.body.username + '!', success: true});
                          }
                        });
                      }
                    });
                  }
            });
          });


    // Verify Token and perform authenticated check
    userRouter.use(function (req, res, next) {

        var token = req.body.token || req.query.token || req.headers['x-access-token'];

        if (token) {
            jwt.verify(token, app.get('secretKey'), function (err, decoded) {
                if (err) {
                    return res.json({success: false, message: 'Failed to authenticate token.'});
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
        .get(function (req, res) {
            // Verify that user is admin
            if (req.decoded._doc.admin) {
                User.find(function (err, users) {
                    if (err) res.send(err);
                    res.json(users);
                });
            } else {
                res.json({success: false, message: "You do not have admin access"});
            }
        });

    // Return all of current user's data
    userRouter.route('/me')
    .get(function(req, res) {
      res.send(req.decoded._doc);
    });


    userRouter.route('/:query_username')
        // GET user data - gather user data for specific username
        .get(function (req, res) {
            // Verify that user is either admin or user to be requested
            if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
                User.findOne({username: req.params.query_username}, function (err, user) {
                    if (err) res.send(err);
                    res.json(user);
                });
            } else {
                res.json({success: false, message: "You do not have access to this page."});
            }
        })

        // PUT user data - change user data for specific username
        .put(function (req, res) {

            // Break if user is not admin or user under question
            if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
                User.findOne({username: req.params.query_username}, function (err, user) {
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

                    user.save(function (err) {
                        if (err) res.send(err);
                        res.json({message: 'User updated!'});
                    });

                });
            } else {
                res.json({success: false, message: "You cannot change this user's information"});
            }
        })


        // DELETE user - delete user for specific username
        .delete(function (req, res) {

            // Break if user is not admin or user under question
            if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
                User.remove({username: req.params.query_username}, function (err, user) {
                    if (err) res.send(err);
                    res.json({message: 'User ' + req.params.query_username + ' successfully deleted'});
                });
            } else {
                res.json({success: false, message: "You do not have access to this page"});
            }
        });

    //getting a user's portfolio (profits from beginning)
    userRouter.route('/portfolios/:query_username').get(function (req, res) {




    });

    /* Below are routes configured for buying and selling stocks

     */

    userRouter.route('/buy/:query_username/:stock_symbol/:quantity')

        //sends info on the transaction, but does not process it
        .get(function (req, res) {
          User.findOne({username: req.decoded._doc.username}, function (err, user) {
              if (err) res.send(err);
              if (req.params.quantity <= 0) {
                res.json({message: "Quantity must be greater than 0"});
              } else {
                mrtScraper(req.params.stock_symbol, function(info) {
                  if(req.params.quantity * info.LastPrice > user.cash) {
                    res.json({message: "You do not have enough money to make this purchase"});
                  } else {
                    res.json({
                      message: "Success",
                      amount: req.params.quantity,
                      costPerShare: info.LastPrice,
                      totalCost: info.LastPrice * req.params.quantity
                    });
                  }
                });
              }
          });
        })

        //performs the act of buying a stock
        .post(function (req, res) {

            User.findOne({username: req.decoded._doc.username}, function (err, user) {
                if (err) res.send(err);
                if (req.params.quantity <= 0) {
                  res.json({message: "Quantity must be greater than 0"});
                } else {
                  mrtScraper(req.params.stock_symbol, function(info) {
                    if(req.params.quantity * info.LastPrice > user.cash) {
                      res.json({message: "You do not have enough money to make this purchase"});
                    } else {
                      Portfolio.findOne({username: req.decoded._doc.username}, function(err, portfolio) {
                        portfolio.userassets.push(new UserAsset({
                          ticker: req.params.stock_symbol,
                          quantity: req.params.quantity,
                          buyPrice: info.LastPrice * req.params.quantity
                        }));
                        portfolio.save(function(err) {
                          if (err) {
                            res.send(err);
                          } else {
                            user.cash -= req.params.quantity * info.LastPrice;
                            user.save(function (err) {
                                if (err) {
                                  res.send(err);
                                } else {

                                  TransactionList.findOne({username: req.decoded._doc.username}, function(err, list) {
                                    list.transactions.push(new Transaction({
                                      stockTicker: req.params.stock_symbol,
                                      type: "Buy",
                                      num_shares: req.params.quantity,
                                      pricePerShare: info.LastPrice,
                                      totalPrice: req.params.quantity * info.LastPrice,
                                      username: req.decoded._doc.username
                                    }));

                                    list.save(function (err) {
                                      if (err) {
                                        res.send(err);
                                      } else {
                                        res.json({
                                          message: "Success",
                                          quantity: req.params.quantity,
                                          costPerShare: info.LastPrice,
                                          totalCost: info.LastPrice * req.params.quantity
                                        });
                                      }
                                    });
                                  });
                                }
                            });
                          }
                        });
                      });
                    }
                  });
                }
                //@TODO: find the number to buy requested, lookup stock price, see if user has enough cash
                //@TODO: add a new transaction to the user associated transaction document
                //@TODO: subtract from the user's cash and add a new stock to their portfolio
                //@TODO: send success message if success, failure message if failure
            });
        });

    userRouter.route('/sell/:query_username/:stock_symbol')

        //sends info on the transaction, but does not process it
        .get(function (req, res) {


        })

        //performs the act of buying a stock
        .post(function (req, res) {

            User.findOne({username: req.decoded._doc.username}, function (err, user) {
                if (err) res.send(err);

                //@TODO: find the number to sell requested, ensure user's quantity >= request quantity
                //@TODO: add a new transaction to the associated document, with % profit
                //@TODO: add to the user's cash and modify their portfolio (remove if selling all stocks)
                //@TODO: send success message if success, failure message if failure
            });
        });

    //for handling requests to /users/transactions (listing transactions)
    require('./transactions')(app, express, User, jwt, Transaction, userRouter);

    app.use('/users', userRouter);
};
