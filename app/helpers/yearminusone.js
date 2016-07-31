dh = require('./datehelper');

module.exports = function(callback) {
  dh((new Date()), callback,(new Date()).getFullYear() - 1);
};
