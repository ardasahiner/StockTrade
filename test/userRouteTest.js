var chai     = require("chai");
var chaiHttp = require("chai-http");
var assert   = chai.assert;
var request  = require("request");
var app      = require("./../server.js")

chai.use(chaiHttp);

describe("User Route Testing (Post, Get, Put, Delete Requests)", function() {
  describe("Create a new user, make some changes, delete the user", function() {

    var domain_url = 'http://localhost:' + app.get('port') + '/';

    it("Creates a new User", function(done) {

      var headers = {}

      var options = {
        url: domain_url + 'users',
        method: 'POST',
        headers: headers,
        form: {
          'username': 'userRouteTest6',
          'password': 'userRouteTest1',
          'email': 'userRouteTest@vStock.io6'
        }
      }

      request(options, function(err, res, body) {
        if (err) console.log(err);
        assert(JSON.parse(body).success == true, "POST request failed");
        done();
      });
      
    });

  });
});
