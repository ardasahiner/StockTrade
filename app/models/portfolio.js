var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;
var UserAsset = require('./userasset').schema;

var PortfolioSchema = new Schema({

  username: {type: String, required: true},
  userassets: {type: [UserAsset]}
});

module.exports = mongoose.model('Portfolio', PortfolioSchema);
