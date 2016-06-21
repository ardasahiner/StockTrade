var chai = require("chai");
var assert = chai.assert;
var eodscraper = require('../scrapers/eodscraper');
var historyscraper = require('../scrapers/historyscraper');

describe("Testing scrapers to ensure they compile and run", function () {
    describe("Using historical scraper and eod scrapers", function () {

        // it("History scraper", function (done) {
        //
        //     historyscraper("tlsa", "daily", 20150619000000, function(results) {
        //
        //       var x = results['symbol']
        //       assert(x == 'tsla', "History scraper failed");
        //       console.log(x);
        //     });
        //     done();
        // });

        it("End of day scraper", function (done) {
          eodscraper("tlsa", function(results) {

          });
          done();
        });

    });
});
