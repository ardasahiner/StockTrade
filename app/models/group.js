var mongoose  = require('mongoose');
var Schema    = mongoose.Schema;
var bcrypt    = require('bcrypt-nodejs');
var ObjectId = Schema.Types.ObjectId;

var GroupSchema = new Schema({
  name: { type: String, required: true, index: { unique : true } },
  groupAdmin: {type: ObjectId, required: true},
  members: {type: [ObjectId], default: [group_admin]}, //idk if this works
  creationDate: {type: Date, default: Date.now()},
  isPrivate: Boolean, //option to be a private group (has a password)
  password: String
});

GroupSchema.pre('save', function(next) {
  var group = this;
  if (!group.isModified('password')) return next();

  bcrypt.hash(group.password, null, null, function(err, hash) {
    group.password = hash;
    next();
  });
});

// Verify password is same as hashed version
GroupSchema.methods.comparePassword = function(password) {
  var group = this;

  //ensure the group has a password to compare to (just in case frontend messes up)
  if (this.isPrivate) {
    return bcrypt.compareSync(password, group.password);
  } else {
    return true;
  }
};


module.exports = mongoose.model('Group', GroupSchema);
