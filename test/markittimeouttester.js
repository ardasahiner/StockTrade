// //Short script to see how many requests per second it takes for markitondemand to time out
// //Results tend to show about 10 requests without any waiting, 100+ if waiting 1 second per request
// var request = require('request');
// var rt = require('../scrapers/realtimescraper');
// //some sample stocks to loop through (in case markit caches if you call for the same stock a bunch)
// var stocks = ['aapl', 'goog', 'tsla', 'bac', 'pg', 'msft', 'gs', 'jpm', 'hp'];
//
// function callForever(numTimes, startTime) {
//   //optional parameter
//   if (typeof numTimes === 'undefined') {
//
//     numTimes = 0;
//   }
//
//   if (typeof startTime === 'undefined') {
//
//     startTime = Date.now();
//   }
//
//   rt(stocks[numTimes % stocks.length], function(response){
//     if (typeof response == 'string') {
//       console.log(1000 * numTimes / ((Date.now() - startTime)) + " requests per second.");
//       console.log(numTimes + " requests total");
//     } else {
//       console.log(response);
//       setTimeout(function() {
//         callForever(numTimes + 1, startTime);
//       }, 1000);
//       console.log("waiting...")
//     }
//   });
// }
//
// module.exports = callForever;
