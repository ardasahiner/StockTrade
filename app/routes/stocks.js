// Stock Router
// Stock Router connects to the Stock Scraper to gather stock price information
var stockDictionary = require('../../vendor/stockdictionary');
var stockDictionaryExchange = require('../../vendor/stockdictionaryexchange');
var reverseStockDictionary = require('../../vendor/stockdictionary');
var mrtScraper = require('../../scrapers/markitrealtimescraper');
var hScraper = require('../../scrapers/historyscraper');
var batslist = require('../../vendor/batslist');
var yearMinusTwo = require('../helpers/yearminustwo');
var yrtScraper = require('../../scrapers/yahoorealtimescraper');


module.exports = function (app, express, User, jwt, currentStockCacheAccurate, currentStockCacheInaccurate) {
  var stockRouter = express.Router();

  //typical middleware for auth
  stockRouter.use(function (req, res, next) {
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

  //This uses Markit on Demand for current data and barchart for historical
  // defaults to daily info for one year
  stockRouter.route('/:stock_symbol').get(function (req, res) {

    // Check to ensure valid stock symbol
    if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
      yearMinusTwo(function(date) {
        console.log(date);
        hScraper(req.params.stock_symbol, 'daily', date, function(historyResult) {
          console.log(historyResult);
          currentStockCacheAccurate.get(req.params.stock_symbol.toUpperCase(), function(err, value) {
            //if not in accurate cache (see design docs for a description of caching mechanism)
            if (err) {
              currentStockCacheInaccurate.get(req.params.stock_symbol.toUpperCase(), function(err, value) {
                //if not in inaccurate cache
                if (err) {
                  mrtScraper(req.params.stock_symbol, function(info) {
                    if (info.Status != 'SUCCESS' || req.params.stock_symbol.toUpperCase() == "GOOG") {
                      yrtScraper(req.params.stock_symbol, function(info) {
                        value = {
                          symbol: req.params.stock_symbol.toUpperCase(),
                          name: stockDictionary[req.params.stock_symbol.toUpperCase()],
                          exchange: stockDictionaryExchange[req.params.stock_symbol.toUpperCase()],
                          lastPrice: parseFloat(info[0][0]).toFixed(2),
                          netChange: parseFloat(info[0][1]).toFixed(2),
                          percentChange: parseFloat(info[0][2].substring(0, info[0][2].length - 1)).toFixed(2), // strips % sign
                          volume: parseInt(info[0][7]),
                          high: parseFloat(parseFloat(info[0][5]).toFixed(2)),
                          low: parseFloat(parseFloat(info[0][6]).toFixed(2)),
                          open: parseFloat(parseFloat(info[0][3]).toFixed(2))
                        };
                        currentStockCacheAccurate.set(req.params.stock_symbol.toUpperCase(), value);
                        res.status(200).json({success: true, message: "success", current: value, past: historyResult});
                      });
                    } else {
                      value = {
                        symbol: info.Symbol.toUpperCase(),
                        name: stockDictionary[info.Symbol.toUpperCase()],
                        exchange: stockDictionaryExchange[info.Symbol.toUpperCase()],
                        lastPrice: info.LastPrice.toFixed(2),
                        netChange: info.Change.toFixed(2),
                        percentChange: info.ChangePercent.toFixed(2),
                        volume: info.Volume,
                        high: info.High,
                        low: info.Low,
                        open: info.Open
                      };
                      currentStockCacheInaccurate.set(info.Symbol.toUpperCase(), value);
                      res.status(200).json({success: true, message: "success", current: value, past: historyResult});
                    }
                  });
                } else {
                  res.status(200).json({success: true, message: "success", current: value, past: historyResult});
                }
              });
            } else {
              res.status(200).json({success: true, message: "success", current: value, past: historyResult});
            }
          });
        });
      });
    } else {

      res.status(404).json({success: false, message: "stock not available", current: "", past: ""});
    }
  });

  // The below routes all give current but partial info about a stock

  // GET the full name corresponding to a given stock symbol
  stockRouter.route('/names/:stock_symbol').get(function (req, res) {
    if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
      res.status(200).json({success: true, result: stockDictionary[req.params.stock_symbol.toUpperCase()]});
    } else {

      res.status(404).json({success: false, result: "stock not available"});
    }
  });

  // GET the exchange corresponding to a given stock symbol
  stockRouter.route('/exchanges/:stock_symbol').get(function (req, res) {
    if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
      res.status(200).json({success: true, result: stockDictionaryExchange[req.params.stock_symbol.toUpperCase()]});
    } else {

      res.status(404).json({success: false, message: "stock not available"});
    }
  });

  stockRouter.route('/history/:stock_symbol/:type/:start_date/:end_date').get(function (req, res) {
    if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
      hScraper(req.params.stock_symbol, req.params.type, req.params.start_date, function(historyResult) {
        res.status(200).json({success: true, message: "success", past: historyResult});
      }, req.params.end_date);
    } else {
      res.status(404).json({success: false, message: "stock not available", past: ""});
    }
  });

  stockRouter.route('/current/:stock_symbol').get(function(req, res) {

    if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
      currentStockCacheAccurate.get(req.params.stock_symbol.toUpperCase(), function(err, value) {

        //if not in accurate cache (see design docs for a description of caching mechanism)
        if (err) {
          currentStockCacheInaccurate.get(req.params.stock_symbol.toUpperCase(), function(err, value) {

            //if not in inaccurate cache
            if(req.params.stock_symbol.toUpperCase())

            if (err) {
              if ((req.params.stock_symbol.toUpperCase()) == "GOOG") {
                yrtScraper(req.params.stock_symbol, function(info) {
                  value = {
                    symbol: req.params.stock_symbol.toUpperCase(),
                    name: stockDictionary[req.params.stock_symbol.toUpperCase()],
                    exchange: stockDictionaryExchange[req.params.stock_symbol.toUpperCase()],
                    lastPrice: parseFloat(info[0][0]).toFixed(2),
                    netChange: parseFloat(info[0][1]).toFixed(2),
                    percentChange: parseFloat(info[0][2].substring(0, info[0][2].length - 1)).toFixed(2), // strips % sign
                    volume: parseInt(info[0][7]),
                    high: parseFloat(parseFloat(info[0][5]).toFixed(2)),
                    low: parseFloat(parseFloat(info[0][6]).toFixed(2)),
                    open: parseFloat(parseFloat(info[0][3]).toFixed(2))
                  };
                  currentStockCacheInaccurate.set(info.Symbol.toUpperCase(), value);
                  res.status(200).json({success: true, message: "success", current: value});
                });
              }
              else {
                mrtScraper(req.params.stock_symbol, function(info) {
                  value = {
                    symbol: info.Symbol.toUpperCase(),
                    name: stockDictionary[info.Symbol.toUpperCase()],
                    exchange: stockDictionaryExchange[info.Symbol.toUpperCase()],
                    lastPrice: info.LastPrice.toFixed(2),
                    netChange: info.Change.toFixed(2),
                    percentChange: info.ChangePercent.toFixed(2),
                    volume: info.Volume,
                    high: info.High,
                    low: info.Low,
                    open: info.Open
                  };
                  currentStockCacheInaccurate.set(info.Symbol.toUpperCase(), value);
                  res.status(200).json({success: true, message: "success", current: value});
                });
              }
            } else {
              res.status(200).json({success: true, message: "success", current: value});
            }
          });
        } else {
          res.status(200).json({success: true, message: "success", current: value});
        }
      });
    } else {
      res.status(404).json({success: false, message: "stock not available", current: ""});
    }
  });

  app.use('/stocks', stockRouter);
};
