var request = require('request');
var keys = require('./barchartkeys');
var keyIndex = 0;

// Accesses end of day data for a given list of stock symbols
// Uses barchart free api
function eodScraper(symbols, fCallback, keyNumber) {

    //optional args
    if (typeof keyNumber === 'undefined') {

      keyNumber = keyIndex;
    }

    // ~~~ s p o o k y r e c u r s i o n ~~~ //
    if (symbols.length > 100) {
      console.log("here we go");
      eodScraper(symbols.slice(0, 100), function(firstResult) {
        console.log("next call: ");
        eodScraper(symbols.slice(100), function(secondResult) {
          fCallback(firstResult.concat(secondResult));
        });
      });
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
              keyIndex += 1;
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
