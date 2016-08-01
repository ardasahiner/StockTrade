var jwt = require('jsonwebtoken');
var User = require('../models/user');
var Transaction = require('../models/transaction');
var TransactionList = require('../models/transactionlist');
var UserAsset = require('../models/userasset');
var NodeCache = require("node-cache");
var currentStockCacheInaccurate = new NodeCache({stdTTL: 240, checkPeriod: 300, errorOnMissing: true});
var currentStockCacheAccurate = new NodeCache({stdTTL: 240, checkPeriod: 300, errorOnMissing: true});

module.exports = function (app, express) {

    // Calls to admin and api routers, adds themselves to the application
    require('./admin')(app, express, User, jwt);
    require('./api')(app, express, User, jwt);
    require('./authentication')(app, express, User, jwt);
    require('./users')(app, express, User, jwt, TransactionList, Transaction, UserAsset, currentStockCacheAccurate);
    require('./stocks')(app, express, User, jwt, currentStockCacheAccurate, currentStockCacheInaccurate);
  
};
