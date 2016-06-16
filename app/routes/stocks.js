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


  // Verify Token and perform authenticated check
  // All following routes should be protected
  stockRouter.use(function(req, res, next) {

    var token = req.body.token || req.query.token || req.headers['x-access-token'];

    if (token) {
      jwt.verify(token, app.get('secretKey'), function(err, decoded) {
        if (err) {
          return res.json({ success : false, message: 'Failed to authenticate token.' });
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


  /* Below are routes for buying and selling a symbol
     Could possibly instead just have these as POST and DELETE requests to ''/:stockname'
     Advantage of below procedure is that it allows client to GET buy and sell requests,
     in case you want to have a "confirm" page before processing a transaction
  */

  stockRouter.route('/buy/:stock_symbol')

  //sends info on the transaction, but does not process it
  .get(function(req, res) {


  })

  //performs the act of buying a stock
  .post(function(req, res) {

    User.findOne({ username: req.decoded._doc.username }, function(err, user) {
      if (err) res.send(err);

      //@TODO: find the number to buy requested, lookup stock price, see if user has enough cash
      //@TODO: add a new transaction to the db
      //@TODO: subtract from the user's cash and add a new stock to their portfolio
      //@TODO: send success message if success, failure message if failure

    });
  });

  stockRouter.route('/sell/:stock_symbol')

  //sends info on the transaction, but does not process it
  .get(function(req, res) {


  })

  //performs the act of selling a stock
  .post(function(req, res) {

    User.findOne({ username: req.decoded._doc.username }, function(err, user) {
      if (err) res.send(err);

      //@TODO: find the number to sell requested, ensure user's quantity >= request quantity
      //@TODO: add a new transaction to the db, with % profit
      //@TODO: add to the user's cash and modify their portfolio (remove if selling all stocks)
      //@TODO: send success message if success, failure message if failure
    });
  });



  app.use('/stocks', stockRouter);
}
