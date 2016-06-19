var openUri = require('open-uri');

// Accesses end of day data for a given list of stock symbols
// Uses barchart free api
function eodScraper(symbols, fCallback, keyNumber) {

    //optional args
    if (keyNumber == 'undefined') {

      keyNumber = 0;
    }
    //callback function passed in to createString
    function innerCallback(symbolsList, kn) {

      if (kn == 'undefined') {

        kn = keyNumber;
      }

      var keys = ["d3aec7bd98718c9fa45caa2d8c12eaeb", "f3b460304a11da7c0bdfe79b17d2b9cf"];
      var url = "http://marketdata.websol.barchart.com/getQuote.json?key=" + keys[kn] + "&symbols=" + symbolsList;
      openUri(url, function (err, info) {
          console.log("url: " + url);
          console.log(info);
          //if not success (aka api key fails), recall with other api key
          if (info["status"]["code"] != 200) {

            innerCallback(symbolsList, (kn + 1) % 2);
          } else {

            //leave it to the callback to process the results (give it the raw data)
            results = info["results"];
            fCallback(resuts);
          }
      });
    }

    createString(symbols, 0, "", innerCallback);
}

// Recursive function to append all stocks in list into a string asynchronously
function createString(symbols, index, currString, callback) {

  if(index >= symbols.length) {
    callback(currString);
  }
  else {
    //updates curr string, then recursively calls
    createString(symbols, index + 1, currString + symbols[index] + ",", callback);
  }
}



module.exports = eodScraper;
