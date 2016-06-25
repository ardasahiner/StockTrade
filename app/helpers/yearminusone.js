dh = require('./datehelper')

module.exports = function(callback) {
  var now = Date.now();
  dh(now, callback, now.getFullYear() - 1);
}
