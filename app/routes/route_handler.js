module.exports = function(app, express) {
  // Calls to admin and api routers, adds themselves to the application
  require('./admin')(app, express);
  require('./api')(app, express);
  require('./users')(app, express);
}
