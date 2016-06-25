var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var bcrypt = require('bcrypt-nodejs');
//var schedule = require('node-schedule');
var UserAsset = require('./userasset');
var HistoricalValue = require('./historicalvalue')

var initialCash = 1000000;

// Basic User Schema built with mongoose
var UserSchema = new Schema({
    // Required tags removed to facilitate testing during development. Add again before production.
    firstName: String,
    lastName: String,

    username: {type: String, required: true, index: {unique: true}},
    password: {type: String, required: true},
    email: {type: String, required: true, index: {unique: true}},
    admin: {type: Boolean, default: false},
    botAccount: {type: Boolean, default: false},
    cash: {type: Number, default: initialCash},
    groups: [String],
    creationDate: {type: Date, default: new Date()},
    portfolio: [UserAsset],
    history: [HistoricalValue]
});


//@TODO: later
//
// //for updating historical data before markets open each day
// var updateHistoricalDataRule = new schedule.RecurrenceRule();
// rule.dayOfWeek = [new schedule.Range(1, 5)]; //monday through friday
// rule.hour = 7; //7 pm
// rule.minute = 0; // minutes
//
// //this occurs every time the conditions above are satisfied
// schedule.scheduleJob(updateHistoricalDataRule, function(){
//
//     var datapoint = new HistoricalValue();
//
// });


// Middleware will be called if there is a save request made.
// If there is a new/changed password, hash it before writing to database
UserSchema.pre('save', function (next) {
    var user = this;
    if (!user.isModified('password')) return next();

    bcrypt.hash(user.password, null, null, function (err, hash) {
        user.password = hash;
        next();
    });
});

// Verify password is same as hashed version
UserSchema.methods.comparePassword = function (password) {
    var user = this;
    return bcrypt.compareSync(password, user.password);
};

// Export UserSchema, bound to Object User
module.exports = mongoose.model('User', UserSchema);
