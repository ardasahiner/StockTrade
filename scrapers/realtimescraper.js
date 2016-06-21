var request = require('request');

//uses markitondemand to get the most recent price of a given stock
function realTimeScraper(symbol, fCallback) {

  var url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=" + symbol;
  request(url, function(error, response, body) {
    if(!error && response.statusCode == 200){
      fCallback(JSON.parse(body));
    } else if (error) {
      console.log(error);
    } else {
      //sent too many requests per second
      fCallback("error, too many requests per second; please wait 30 seconds");
    }
  });
}

module.exports = realTimeScraper;
