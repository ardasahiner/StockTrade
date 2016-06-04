// Stock Router
// Stock Router connects to the Stock Scraper to gather stock price information
module.exports = function(app, express) {
  var stockRouter = express.Router();

  var scraper = require('../../scrapers/stock_scraper');

  stockRouter.route('/:stock_symbol').get(function(req, res) {
    scraper(req.params.stock_symbol, 'll', function(stock_price) {
      res.send(stock_price);
    });
  })

  app.use('/stock', stockRouter);
}
