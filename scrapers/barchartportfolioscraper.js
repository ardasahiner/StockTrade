var request = require('request');
var keys = require('./barchartkeys');

// Accesses end of day data for a given list of stock symbols
// Uses barchart free api
function eodScraper(symbols, fCallback, keyNumber) {

    //optional args
    if (typeof keyNumber === 'undefined') {

      keyNumber = 0;
    }
    // callback function passed in to createString
    function innerCallback(symbolsList, kn) {
      if (typeof kn === 'undefined') {
        kn = keyNumber;
      }

      var url = "http://marketdata.websol.barchart.com/getQuote.json?key=" + keys[kn] + "&symbols=" + symbolsList;
      request(url, function(error, response, body) {

        if(!error && response.statusCode == 200){
          try{
            fCallback(JSON.parse(body)['results']);
          } catch(err) {
            //try again with other api key
            console.log("Key " + kn +  " ran out");
            if (kn < keys.length - 1) {
              innerCallback(symbolsList, kn + 1);
            } else{
              fCallback({message: "Error"});
            }
          }
        } else if (error) {
          console.log(error);
        } else {
          fCallback({message: "Error"});
        }
      });
    }

    createString(symbols, 0, "", innerCallback);
}

// Recursive function to append all stocks in list into a string asynchronously
function createString(symbols, index, currString, callback) {

  if(index >= symbols.length) {
    callback(currString);
  } else if (typeof symbols === 'string') {

    callback(symbols);
  } else {
    //updates curr string, then recursively calls
    createString(symbols, index + 1, currString + symbols[index] + ",", callback);
  }
}



module.exports = eodScraper;
