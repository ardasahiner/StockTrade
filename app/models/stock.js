var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;

var StockSchema = new Schema({

  ticker: {type: String, required: true, index: {unique: true}},
  fullName: {type: String, required: true}
});

module.exports = mongoose.model('Stock', StockSchema);