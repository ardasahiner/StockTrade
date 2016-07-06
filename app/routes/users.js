var mrtScraper = require('../../scrapers/markitrealtimescraper');
var async = require('async');
var bScraper = require('../../scrapers/barchartportfolioscraper');

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
            user.botAccount = req.body.bot;

            // callback
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
                          res.json({message: 'User created! Welcome ' + req.body.username + '!', success: true});
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

    //getting a user's portfolio (profits from beginning)
    userRouter.route('/portfolios').get(function (req, res) {

      UserAsset.find({username: req.decoded._doc.username}, function(err, assets) {
        var tickerList = [];

        async.forEach(assets, function(asset, callback) {

          tickerList.push(asset.ticker);
          callback();
        }, function(err) {

          bScraper(tickerList, function(infoList) {
            User.findOne({username: req.decoded._doc.username}, function(err, user) {
              var response = {username: user.username, cash: user.cash, assets: []};
              var portfolioValue = user.cash;
              console.log(portfolioValue);
              async.forEach(infoList, function(currentInfo, callback) {
                UserAsset.find({username: user.username, ticker: currentInfo.symbol}, function(err, asset) {
                  portfolioValue += asset[0].quantity * currentInfo.lastPrice;
                  


                  callback();
                });
              }, function(err){
                console.log(portfolioValue);

              });
            });
          });
        });
      });
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

    /* Below are routes configured for buying and selling stocks
     */
    userRouter.route('/buy/:query_username/:stock_symbol/:quantity')

        //sends info on the transaction, but does not process it
        .get(function (req, res) {
          // Break if user is not admin or user under question
          if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
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
          } else {
            res.json({success: false, message: "You do not have access to this page"});
          }
        })

        //performs the act of buying a stock
        .post(function (req, res) {

            // Arda's most disgusting block of code ever :)
            // Break if user is not admin or user under question
            if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
              User.findOne({username: req.decoded._doc.username}, function (err, user) {
                  if (err) res.send(err);
                  if (req.params.quantity <= 0) {
                    res.json({message: "Quantity must be greater than 0"});
                  } else {
                    mrtScraper(req.params.stock_symbol, function(info) {
                      if(req.params.quantity * info.LastPrice > user.cash) {
                        res.json({message: "You do not have enough money to make this purchase"});
                      } else {
                        UserAsset.findOne({username: req.decoded._doc.username, ticker: req.params.stock_symbol}, function(err, asset) {
                          //doesn't exist yet
                          if (err) {
                            res.send(err);
                          } else {
                            console.log(asset === null);
                            if (asset === null) {
                              var asset = new UserAsset();
                              asset.ticker = req.params.stock_symbol;
                              asset.quantity = req.params.quantity;
                              asset.buyPrice = info.LastPrice * req.params.quantity;
                              asset.username = req.decoded._doc.username;
                            } else {
                              asset.quantity += parseInt(req.params.quantity);
                              asset.buyPrice += info.LastPrice * req.params.quantity;
                            }
                          }
                          asset.save(function(err) {
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
              });
            } else {
              res.json({success: false, message: "You do not have access to this page"});
            }
        });

    userRouter.route('/sell/:query_username/:stock_symbol/:quantity')

        //sends info on the transaction, but does not process it
        .get(function (req, res) {
          if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
            User.findOne({username: req.decoded._doc.username}, function(err, user) {
              if (err) {
                res.send(err);
              } else if (req.params.quantity <= 0) {
                  res.json({message: "Quantity must be greater than 0"});
              } else {
                UserAsset.findOne({username: req.decoded._doc.username, ticker: req.params.stock_symbol}, function(err, asset) {
                  if (err) {res.send(err);}
                  else if (asset === null) {
                    res.json({message: "You do not own this stock, so you cannot sell it"});
                  } else if (asset.quantity < req.params.quantity) {
                    res.json({message: "You do not own as many of this stock as you are attempting to sell"});
                  } else {
                    mrtScraper(req.params.stock_symbol, function(info) {
                      res.json({
                        message: "Success",
                        quantity: req.params.quantity,
                        revenuePerShare: info.LastPrice,
                        totalRevenue: info.LastPrice * req.params.quantity
                      });
                    });
                  }
                });
              }
            });
          } else {
            res.json({success: false, message: "You do not have access to this page"});
          }
        })

        //performs the act of buying a stock
        .post(function (req, res) {
          if (req.decoded._doc.admin || req.decoded._doc.username == req.params.query_username) {
            User.findOne({username: req.decoded._doc.username}, function (err, user) {
              if (err) {
                res.send(err);
              } else if (req.params.quantity <= 0) {
                  res.json({message: "Quantity must be greater than 0"});
              } else {
                UserAsset.findOne({username: req.decoded._doc.username, ticker: req.params.stock_symbol}, function(err, asset) {
                  if (err) {res.send(err);}
                  else if (asset === null) {
                    res.json({message: "You do not own this stock, so you cannot sell it"});
                  } else if (asset.quantity < req.params.quantity) {
                    res.json({message: "You do not own as many of this stock as you are attempting to sell"});
                  } else {
                    mrtScraper(req.params.stock_symbol, function(info) {
                      var prevQuantity = asset.quantity;
                      var prevPrice = asset.buyPrice;
                      if (asset.quantity === parseInt(req.params.quantity)) {
                        asset.remove(function(err) {
                          sellHelper(err, user, info, res, req, prevQuantity, prevPrice, TransactionList, Transaction);
                        });

                      } else {
                        asset.quantity -= parseInt(req.params.quantity);
                        asset.buyPrice -= parseInt(info.LastPrice * req.params.quantity);
                        asset.save(function (err) {
                          sellHelper(err, user, info, res, req, prevQuantity, prevPrice, TransactionList, Transaction);
                        });
                      }
                    });
                  }
                });
              }

                //@TODO: find the number to sell requested, ensure user's quantity >= request quantity
                //@TODO: add a new transaction to the associated document, with % profit
                //@TODO: add to the user's cash and modify their portfolio (remove if selling all stocks)
                //@TODO: send success message if success, failure message if failure
            });
          } else {
            res.json({success: false, message: "You do not have access to this page"});
          }
        });

    //for handling requests to /users/transactions (listing transactions)
    require('./transactions')(app, express, User, jwt, Transaction, userRouter);

    app.use('/users', userRouter);
};

// helper for sell POST route (so I don't have to copy paste the same thing)
var sellHelper = function(err, user, info, res, req, prevQuantity, prevPrice, TransactionList, Transaction) {
  if (err) {
    res.send(err);
  } else {
    user.cash += info.LastPrice * req.params.quantity;
    user.save(function(err) {
      if (err) {
        res.send(err);
      } else {
        TransactionList.findOne({username: req.decoded._doc.username}, function(err, list) {
          list.transactions.push(new Transaction({
            stockTicker: req.params.stock_symbol,
            type: "Sell",
            num_shares: req.params.quantity,
            pricePerShare: info.LastPrice,
            totalPrice: req.params.quantity * info.LastPrice,
            username: req.decoded._doc.username,
            percentProfit: (info.LastPrice / (prevPrice / prevQuantity) - 1) * 100
          }));

          list.save(function (err) {
            if (err) {
              res.send(err);
            } else {
              res.json({
                message: "Success",
                quantity: req.params.quantity,
                revenuePerShare: info.LastPrice,
                totalRevenue: info.LastPrice * req.params.quantity
              });
            }
          });
        });
      }
    });
  }
};
