var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');

var GroupSchema = new Schema({
    name: {type: String, required: true, index: {unique: true}},
    groupAdminName: {type: String, required: true},
    memberNames: [String] // remember to push group admin's ID before saving
    creationDate: {type: Date, default: new Date()},
    isPrivate: Boolean, //option to be a private group (has a password)
    password: String
});

GroupSchema.pre('save', function (next) {
    var group = this;
    if (!group.isModified('password')) return next();

    bcrypt.hash(group.password, null, null, function (err, hash) {
        group.password = hash;
        next();
    });
});

// Verify password is same as hashed version
GroupSchema.methods.comparePassword = function (password) {
    var group = this;

    //ensure the group has a password to compare to (just in case frontend messes up)
    if (this.isPrivate) {
        return bcrypt.compareSync(password, group.password);
    } else {
        return true;
    }
};


module.exports = mongoose.model('Group', GroupSchema);
