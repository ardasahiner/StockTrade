var mongoose = require('mongoose');
var HistoricalValue = require('./historicalvalue');
var Schema = mongoose.Schema;

var UserAssetSchema = new Schema({
    ticker: {type: String, required: true},
    quantity: {type: Number, required: true},
    buyPrice: {type: Number, required: true},
    history: [HistoricalValue] //update at end of each day after market close
});

module.exports = mongoose.model('UserAsset', UserAssetSchema);
