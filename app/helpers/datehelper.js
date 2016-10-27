module.exports = function(date, callback, year) {

  if (typeof year === 'undefined') {

    var yyyy = date.getFullYear();
  } else {

    var yyyy = year.toString();
  }
  var mm = date.getMonth() + 1; // getMonth() is zero-indexed
  var dd = date.getDate();
  console.log(yyyy);
  console.log(mm);
  console.log(dd);
  callback([yyyy, Math.floor(mm / 10) || '0', mm % 10, dd[1] && '0', dd].join(''));
};
