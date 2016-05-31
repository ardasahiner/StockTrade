var openUri = require('open-uri');
var test = 'test';
var stock_value;
var done = false;

// This function executes the scraper and queries the requested data from Yahoo Finance
function stock_scraper(symbol, stat, cb) {
  done = false;
  var url = "http://finance.yahoo.com/d/quotes.csv?s=" + symbol + "&f=" + stat;
  openUri(url, function(err, stock) {
    var stock_data =stock.toString('utf8');
    var stock_price = />([^<]+)</.exec(stock_data)[1];

    // Logs Stock Price to Console, TODO: implement callback so that this can be efficiently used
    // console.log(stock_price);
    cb(stock_price);
    done = true;
    stock_value = stock_price;
  });
}

exports.done = done;
exports.stock_value = stock_value;
exports.test = test;
exports.stock_scraper = stock_scraper; //public function
