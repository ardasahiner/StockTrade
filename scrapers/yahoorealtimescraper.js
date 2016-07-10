var request = require('request');

//uses markitondemand to get the most recent price of a given stock
function realTimeScraper(symbol, fCallback) {

  var url = "http://finance.yahoo.com/webservice/v1/symbols/" + symbol + "/quote?format=json";
  request(url, function(error, response, body) {
    if(!error && response.statusCode == 200){
      fCallback(JSON.parse(body)["list"]["resources"][0]["resource"]["fields"]);
    } else if (error) {
      console.log(error);
    } else {
      //sent too many requests per second
      fCallback("error, too many requests");
    }
  });
}

module.exports = realTimeScraper;
