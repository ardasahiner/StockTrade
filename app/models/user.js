var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');

// Basic User Schema built with mongoose
var UserSchema = new Schema({
  name: String,
  username: { type: String, required: true, index: { unique : true }},
  password: { type: String, required: true, select: false }
});

// If there is a new/changed password, hash it before writing to database
UserSchema.pre('save', function(next) {
  var user = this;
  if (!user.isModified('password')) return next();

  bcrypt.hash(user.password, null, null, function(err, hash) {
    user.password = hash;
    next();
  });
});

// Verify password is same as hashed version
UserSchema.methods.comparePassword = function(password) {
  var user = this;
  return bcrypt.compareSync(password, user.password);
};

module.exports = mongoose.model('User', UserSchema);
