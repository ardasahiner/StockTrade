// Stock Router
// Stock Router connects to the Stock Scraper to gather stock price information
var stockDictionary = require('../../vendor/stockdictionary');
var stockDictionaryExchange = require('../../vendor/stockdictionaryexchange');
var reverseStockDictionary = require('../../vendor/stockdictionary');
var mrtScraper = require('../../scrapers/markitrealtimescraper');
var hScraper = require('../../scrapers/historyscraper');
var batslist = require('../../vendor/batslist');
var yearMinusOne = require('../helpers/yearminusone');

module.exports = function (app, express, User, jwt) {
    var stockRouter = express.Router();

    //typical middleware for auth
    stockRouter.use(function (req, res, next) {
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

    /* This route should send all info about a stock in json format:
    Name of the company
    The company's ticker symbol
    The last price of the company's stock
    The change in price of the company's stock since the previous trading day's close
    The change percent in price of the company's stock since the previous trading day's close
    The last time the company's stock was traded in exchange-local timezone. Represented as ddd MMM d HH:mm:ss UTCzzzzz yyyy
    The last time the company's stock was traded in exchange-local timezone. Represented as an OLE Automation date
    The company's market cap
    The trade volume of the company's stock
    The change in price of the company's stock since the start of the year
    The change percent in price of the company's stock since the start of the year
    The high price of the company's stock in the trading session
    The low price of the company's stock in the trading session
    The opening price of the company's stock at the start of the trading session
    Daily history regarding stock (for one year) */

    //NOTE: This uses Markit on Demand for current data and barchart for historical
    // defaults to daily info for one year
    stockRouter.route('/:stock_symbol').get(function (req, res) {

        // Check to ensure valid stock symbol
        if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
          mrtScraper(req.params.stock_symbol, function (markitResult) {
            yearMinusOne(function(date) {
              hScraper(req.params.stock_symbol, 'daily', date, function(historyResult) {
                  res.status(200).json({message: "success", current: markitResult, past: historyResult});
              });
            });
          });
        } else {

          res.status(400).json({message: "stock not available", current: "", past: ""});
        }
    });

    // The below routes all give current but partial info about a stock

    // GET the full name corresponding to a given stock symbol
    stockRouter.route('/names/:stock_symbol').get(function (req, res) {
      if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
        res.send(stockDictionary[req.params.stock_symbol.toUpperCase()]);
      } else {

        res.json(404, {message: "stock not available"});
      }
    });

    // GET the exchange corresponding to a given stock symbol
    stockRouter.route('/exchanges/:stock_symbol').get(function (req, res) {
      if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
        res.send(stockDictionaryExchange[req.params.stock_symbol.toUpperCase()]);
      } else {

        res.json(404, {message: "stock not available"});
      }
    });

    stockRouter.route('/history/:stock_symbol/:type/:start_date/:end_date').get(function (req, res) {
      if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
        hScraper(req.params.stock_symbol, req.params.type, req.params.start_date, function(historyResult) {

          res.json(historyResult);
        }, req.params.end_date);
      } else {

        res.json(404, {message: "stock not available"});
      }
    });

    stockRouter.route('/current/:stock_symbol').get(function(req, res) {
      if (batslist.indexOf(req.params.stock_symbol.toUpperCase()) > -1) {
        mrtScraper(req.params.stock_symbol, function(result) {
          res.json(result);
        }, req.params.end_date);
      } else {

        res.json(404, {message: "stock not available"});
      }
    });

    app.use('/stocks', stockRouter);
};
