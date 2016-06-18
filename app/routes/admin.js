// Administrator Router
// Admin Router will communicate administrative information
// Admin authentication requires user to have admin access (all routes secured)
module.exports = function (app, express, User, jwt) {
    var adminRouter = express.Router();

    // Verify Token and Admin Status
    adminRouter.use(function (req, res, next) {

        var token = req.body.token || req.query.token || req.headers['x-access-token'];

        if (token) {

            jwt.verify(token, app.get('secretKey'), function (err, decoded) {
                if (err) {
                    return res.json({success: false, message: 'Failed to authenticate token.'});
                } else {
                    // Decoded token saved into request parameters
                    req.decoded = decoded;
                    if (!req.decoded._doc.admin) {
                        return res.json({success: false, message: 'You do not have admin access'});
                    }
                    next();
                }
            });

        } else {
            // No token provided
            return res.status(403).send({
                success: false,
                message: 'No token provided.'
            });
        }
    });

    adminRouter.get('/', function (req, res) {
        res.send('Admin Dashboard');
    });

    // Access administrative user data - priviledged data access
    adminRouter.get('/users', function (req, res) {
        res.send('User Data');
    });

    app.use('/admin', adminRouter);
};
