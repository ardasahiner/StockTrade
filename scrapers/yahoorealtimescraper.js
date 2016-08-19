var request = require('request');
var parse = require('csv-parse');

// uses yahoo for most recent price, change, change in percent, open, close, high, low and volume
// in that order
// Calls callback on array, with indices in order of the request
function yahooScraper(symbol, fCallback) {

  var url = "http://download.finance.yahoo.com/d/quotes.csv?s=" + symbol + "&f=l1c1p2ophgv";
  request(url, function(error, response, body) {
    if(!error && response.statusCode == 200){
      parse(body, function(err, output) {
        if (err) fCallback(err);
        else {
          fCallback(output);
        }
      });
    } else {
      fCallback({message: "something went wrong!"});
    }
  });
}

module.exports = yahooScraper;
