var jwt   = require('jsonwebtoken');
var User  = require('../models/user');
var stockDictionary = require('../../vendor/stockdict');
var Transaction = require('../models/transaction');
var TransactionList = require('../models/transactionlist');
var UserAsset = require('../models/userasset')

module.exports = function(app, express) {

  // Calls to admin and api routers, adds themselves to the application
  require('./admin')(app, express, User, jwt);
  require('./api')(app, express, User, jwt);
  require('./authentication')(app, express, User, jwt);
  require('./users')(app, express, User, jwt, TransactionList, Transaction, UserAsset);
  require('./stocks')(app, express, User, jwt, stockDictionary);
};
