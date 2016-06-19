var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var HistoricalValue = new Schema({
    date: {type: Date, required: true},
    value: {type: Number, required: true}  //total value of a user's assets
});

module.exports = mongoose.model('HistoricalValue', HistoricalValue);
