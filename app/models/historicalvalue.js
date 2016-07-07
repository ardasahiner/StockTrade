var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var HistoricalValue = new Schema({
  date: {type: Date, required: true},
  value: {type: Number, required: true}  // value of an asset (or group of assets)
});

module.exports = mongoose.model('HistoricalValue', HistoricalValue);
