var mrtScraper = require('../../scrapers/markitrealtimescraper');
var async = require('async');
var bScraper = require('../../scrapers/barchartportfolioscraper');
var batslist = require('../../vendor/batslist');

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
                    res.json({success: false, message : err});
                  } else {
                    var tl = new TransactionList();
                    tl.username = req.body.username;
                    tl.save(function (err) {
                      if (err) {
                        // TODO: Add custom error messages that can be displayed to the user, the current ones make no sense
                        // TODO: This kind of a thing is done in the Authentication Route for example
                        res.json({success: false, message : "Username or email not unique"});
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
    userRouter.route('/portfolio').get(function (req, res) {

      UserAsset.find({username: req.decoded._doc.username}, function(err, assets) {
        var tickerList = [];

        async.forEach(assets, function(asset, callback) {

          tickerList.push(asset.ticker);
          callback();
        }, function(err) {

          bScraper(tickerList, function(infoList) {
            User.findOne({username: req.decoded._doc.username}, function(err, user) {
              var response = {username: user.username, cash: user.cash.toFixed(2), assets: []};
              var portfolioValue = parseFloat(user.cash.toFixed(2));
              async.forEach(infoList, function(currentInfo, callback) {
                if (currentInfo !== "Error") {
                  UserAsset.find({username: user.username, ticker: currentInfo.symbol.toUpperCase()}, function(err, asset) {
                    portfolioValue += parseFloat((asset[0].quantity * currentInfo.lastPrice).toFixed(2));
                    response.assets.push({ticker: currentInfo.symbol.toUpperCase(),
                                          name: currentInfo.name,
                                          exchange: currentInfo.exchange,
                                          quantity: asset[0].quantity.toFixed(0),
                                          pricePerShare: currentInfo.lastPrice.toFixed(2),
                                          amountSpent: asset[0].buyPrice.toFixed(2),
                                          currentValue: (asset[0].quantity * currentInfo.lastPrice).toFixed(2),
                                          amountProfit: (asset[0].quantity * currentInfo.lastPrice - asset[0].buyPrice).toFixed(2),
                                          percentProfit: (((asset[0].quantity * currentInfo.lastPrice) / asset[0].buyPrice - 1) * 100).toFixed(2)});
                  });
                }
                callback();
              }, function(err){
                response.portfolioValue = portfolioValue.toFixed(2);
                response.grossProfit = (portfolioValue - 1000000).toFixed(2);
                response.percentProfit = ((portfolioValue / 1000000 - 1) * 100).toFixed(2);
                res.send(response);
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

    userRouter.route('/buy/:stock_symbol/:quantity')

        //sends info on the transaction, but does not process it
        .get(function (req, res) {
          //stock does not exist
          if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) < 0) {
            res.json({success: false, message: "The stock you attempted to buy does not exist"});
          } else {
            User.findOne({username: req.decoded._doc.username}, function (err, user) {
                if (err) res.send(err);
                if (req.params.quantity <= 0) {
                  res.json({success: false, message: "Quantity must be greater than 0"});
                } else {
                  mrtScraper(req.params.stock_symbol, function(info) {
                    if(parseFloat((req.params.quantity * info.LastPrice).toFixed(2)) > user.cash) {
                      res.json({success: false, message: "You do not have enough money to make this purchase"});
                    } else {
                      res.json({
                        message: "GET Success",
                        amount: req.params.quantity,
                        costPerShare: info.LastPrice.toFixed(2),
                        totalCost: (info.LastPrice * req.params.quantity).toFixed(2),
                        success: true
                      });
                    }
                  });
                }
            });
          }
        })

        //performs the act of buying a stock
        .post(function (req, res) {
          if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) < 0) {
            res.json({sucess: false, message: "The stock you attempted to buy does not exist"});
          } else {
            // Arda's most disgusting block of code ever :)
              User.findOne({username: req.decoded._doc.username}, function (err, user) {
                  if (err) res.send(err);
                  if (req.params.quantity <= 0) {
                    res.json({message: "Quantity must be greater than 0"});
                  } else {
                    mrtScraper(req.params.stock_symbol, function(info) {
                      if(parseFloat((req.params.quantity * info.LastPrice).toFixed(2)) > user.cash) {
                        res.json({message: "You do not have enough money to make this purchase"});
                      } else {
                        UserAsset.findOne({username: req.decoded._doc.username, ticker: req.params.stock_symbol.toUpperCase()}, function(err, asset) {
                          //doesn't exist yet
                          if (err) {
                            res.send(err);
                          } else {
                            if (asset === null) {
                              var asset = new UserAsset();
                              asset.ticker = req.params.stock_symbol.toUpperCase();
                              asset.quantity = req.params.quantity;
                              asset.buyPrice = parseFloat((info.LastPrice * req.params.quantity).toFixed(2));
                              asset.username = req.decoded._doc.username;
                            } else {
                              asset.quantity += parseInt(req.params.quantity);
                              asset.buyPrice += parseFloat((info.LastPrice * req.params.quantity).toFixed(2));
                            }
                          }
                          asset.save(function(err) {
                            if (err) {
                              res.send(err);
                            } else {
                              user.cash -= parseFloat((req.params.quantity * info.LastPrice).toFixed(2));
                              user.save(function (err) {
                                  if (err) {
                                    res.send(err);
                                  } else {
                                    TransactionList.findOne({username: req.decoded._doc.username}, function(err, list) {
                                      list.transactions.push(new Transaction({
                                        stockTicker: req.params.stock_symbol.toUpperCase(),
                                        type: "Buy",
                                        num_shares: req.params.quantity,
                                        pricePerShare: info.LastPrice,
                                        totalPrice: (req.params.quantity * info.LastPrice),
                                        username: req.decoded._doc.username
                                      }));

                                      list.save(function (err) {
                                        if (err) {
                                          res.send(err);
                                        } else {
                                          res.json({
                                            message: "POST Success",
                                            quantity: req.params.quantity,
                                            costPerShare: info.LastPrice.toFixed(2),
                                            totalCost: (info.LastPrice * req.params.quantity).toFixed(2)
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
            }
        });

    userRouter.route('/sell/:stock_symbol/:quantity')

        //sends info on the transaction, but does not process it
        .get(function (req, res) {
            User.findOne({username: req.decoded._doc.username}, function(err, user) {
              if (err) {
                res.send(err);
              } else if (req.params.quantity <= 0) {
                  res.json({success: false, message: "Quantity must be greater than 0"});
              } else {
                UserAsset.findOne({username: req.decoded._doc.username, ticker: req.params.stock_symbol.toUpperCase()}, function(err, asset) {
                  if (err) {res.send(err);}
                  else if (asset === null) {
                    res.json({success: false, message: "You do not own this stock, so you cannot sell it"});
                  } else if (asset.quantity < req.params.quantity) {
                    res.json({success: false, message: "You do not own as many of this stock as you are attempting to sell"});
                  } else {
                    mrtScraper(req.params.stock_symbol, function(info) {
                      res.json({
                        message: "GET Success",
                        quantity: req.params.quantity,
                        revenuePerShare: info.LastPrice.toFixed(2),
                        totalRevenue: (info.LastPrice * req.params.quantity).toFixed(2)
                      });
                    });
                  }
                });
              }
            });
        })

        //performs the act of buying a stock
        .post(function (req, res) {
            User.findOne({username: req.decoded._doc.username}, function (err, user) {
              if (err) {
                res.send(err);
              } else if (req.params.quantity <= 0) {
                  res.json({message: "Quantity must be greater than 0"});
              } else {
                UserAsset.findOne({username: req.decoded._doc.username, ticker: req.params.stock_symbol.toUpperCase()}, function(err, asset) {
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
                        asset.buyPrice -= parseFloat((info.LastPrice * req.params.quantity).toFixed(2));
                        asset.save(function (err) {
                          sellHelper(err, user, info, res, req, prevQuantity, prevPrice, TransactionList, Transaction);
                        });
                      }
                    });
                  }
                });
              }
            });
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
    user.cash += parseFloat((info.LastPrice * req.params.quantity).toFixed(2));
    user.save(function(err) {
      if (err) {
        res.send(err);
      } else {
        TransactionList.findOne({username: req.decoded._doc.username}, function(err, list) {
          list.transactions.push(new Transaction({
            stockTicker: req.params.stock_symbol.toUpperCase(),
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
                message: "POST Success",
                quantity: req.params.quantity,
                revenuePerShare: info.LastPrice.toFixed(2),
                totalRevenue: (info.LastPrice * req.params.quantity).toFixed(2)
              });
            }
          });
        });
      }
    });
  }
};
