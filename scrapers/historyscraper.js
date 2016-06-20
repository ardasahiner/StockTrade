var openUri = require('open-uri');

// Accesses historical data for a given stock symbol, type (daily, minutes, weekly, etc.), start date and
// end date (optional), and callback
// Uses barchart free api
function historicalStockScraper(symbol, type, startDate, fCallback, endDate, keyNumber) {

    // optional arguments
    if (endDate == 'undefined') {

      endDate = "null";
    }
    if (keyNumber == 'undefined') {

      keyNumber = 0;
    }

    var keys = ["d3aec7bd98718c9fa45caa2d8c12eaeb", "f3b460304a11da7c0bdfe79b17d2b9cf"];

    var url = "http://marketdata.websol.barchart.com/getHistory.json?key=" + keys[keyNumber] + "&symbol=" + symbol;
    url += "&type=" + type + "&startDate=" + startDate + "&endDate=" + endDate;
    openUri(url, function (err, history) {

        //if not success (aka api key fails), recall with other api key
        //@TODO: probably change this to be cooler
        if (history["status"]["code"] != 200) {

          historicalStockScraper(symbol, type, startDate, fCallback, endDate, (keyNumber + 1) % 2);
        } else {

          //leave it to the callback to process the results (give it the raw data)
          results = history["results"];
          fCallback(resuts);
        }
    });
}

module.exports = historicalStockScraper;
