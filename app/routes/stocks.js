// Stock Router
// Stock Router connects to the Stock Scraper to gather stock price information
module.exports = function(app, express, User, jwt, stockDictionary) {
  var stockRouter = express.Router();

  var scraper = require('../../scrapers/stock_scraper');

  //@TODO: this route should send all info about a stock in json format, not just price
  stockRouter.route('/:stock_symbol').get(function(req, res) {

    //@TODO: check to ensure valid stock symbol
    scraper(req.params.stock_symbol, 'll', function(stock_price) {
      res.send(stock_price);
    });
  });

  // GET the full name corresponding to a given stock symbol
  stockRouter.route('/:stock_symbol/name').get(function(req, res) {

      res.send(stockDictionary[req.params.stock_symbol]);
  });

  //@TODO: additional routes for getting info on stocks (value at a given date, percent change
  // from a given date, p/e ratio, market cap, what exchange it's traded in, etc.)


  app.use('/stocks', stockRouter);
};
