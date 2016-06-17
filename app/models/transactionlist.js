var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;
var ObjectId = Schema.Types.ObjectId;
var Transaction = require('./transaction')


var TransactionListSchema = new Schema({

  userId: {type: ObjectId, required: true},
  transactionList: {type: [Transaction]}
});

module.exports = mongoose.model('TransactionList', TransactionListSchema);
