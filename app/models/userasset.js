var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;

var UserAssetSchema = new Schema({
  ticker: { type: String, required: true },
  quantity: {type: Number, required: true },
});

module.exports = mongoose.model('UserAsset', UserAssetSchema);
