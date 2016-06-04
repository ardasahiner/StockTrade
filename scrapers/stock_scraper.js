var openUri = require('open-uri');

// This function executes the scraper and queries the requested data from Yahoo Finance
function stock_scraper(symbol, stat, fCallback) {
  done = false;
  var url = "http://finance.yahoo.com/d/quotes.csv?s=" + symbol + "&f=" + stat;
  openUri(url, function(err, stock) {

    var stock_data =stock.toString('utf8');
    var stock_price = />([^<]+)</.exec(stock_data)[1];

    fCallback(stock_price);
  });
}

module.exports = stock_scraper;
