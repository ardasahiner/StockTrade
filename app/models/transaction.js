var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;
var ObjectId = Schema.Types.ObjectId;

var InnerSchema = new Schema({

  stockTicker:  {type: String, required: true },
  type: {type: String, required: true },
  num_shares: {type: Number, required: true },
  pricePerShare: {type: Number, required: true },
  totalPrice: {type: Number, required: true },
  percentProfit: Number,
  transactionDate: {type: Date, default: Date.now()},
  username: {type: String, required: true}
});


var TransactionSchema = new Schema({

  userId: {type: ObjectId, required: true},
  transactionList: {type: [InnerSchema], default: []}
});

module.exports = mongoose.model('Transaction', TransactionSchema);
