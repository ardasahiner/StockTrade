// API Router will communicate user information with the front end
module.exports = function (app, express, User, jwt) {
    var apiRouter = express.Router();

    // Access API dashboard
    apiRouter.get('/', function (req, res) {
        res.send('API Dashboard');
    });

    app.use('/api_dashboard', apiRouter);
};
