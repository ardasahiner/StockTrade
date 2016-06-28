var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;
var ObjectId = Schema.Types.ObjectId;
var Transaction = require('./transaction')

var TransactionListSchema = new Schema({

  username: {type: String, required: true},
  transactions: {type: [Transaction]}
});

module.exports = mongoose.model('TransactionList', TransactionListSchema);
