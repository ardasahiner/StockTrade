var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;

var TransactionSchema = new Schema({

  stock_ticker:  {type: String, required: true },
  type: {type: String, required: true },
  num_shares: {type: Number, required: true },
  price_per_share: {type: Number, required: true },
  total_price: {type: Number, required: true },
  percent_profit: Number
});


module.exports = mongoose.model('Transaction', TransactionSchema);
