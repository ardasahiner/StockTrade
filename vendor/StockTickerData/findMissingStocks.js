var bl = require('../batslist');
var sd = require('../stockdictionary');
var async = require('async');
var list = [];

async.forEach(bl, function(ticker, callback) {

  if (typeof sd[ticker] == 'undefined') {

    list.push(ticker);
    callback();
  } else {
    callback();
  }
});

module.exports = list.length;
