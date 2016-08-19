var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;
var Transaction = require('./transaction').schema;

var TransactionListSchema = new Schema({

  username: {type: String, required: true},
  transactions: {type: [Transaction]}
});

module.exports = mongoose.model('TransactionList', TransactionListSchema);
