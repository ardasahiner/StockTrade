module.exports = function(date, callback, year) {

  if (typeof year === 'undefined') {

    var yyyy = date.getFullYear();
  } else {

    var yyyy = year.toString();
  }
  var mm = date.getMonth() + 1; // getMonth() is zero-indexed 
  var dd = date.getDate();
  callback([yyyy, !mm[1] && '0', mm, dd[1] && '0', dd].join(''));
};
