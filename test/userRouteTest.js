var chai     = require("chai");
var assert   = chai.assert;
var request  = require("request");
var app      = require("./../server.js");

describe("User Route Testing (Post, Get, Put, Delete Requests)", function() {
  describe("Create a new user, make some changes, delete the user", function() {

    var domain_url = 'http://localhost:' + app.get('port') + '/';
    var testUser = "userRouteTester4";
    var token = "";

    it("Creates a new User", function(done) {

      var headers = {};

      var options = {
        url: domain_url + 'users',
        method: 'POST',
        headers: headers,
        form: {
          'username': testUser,
          'password': testUser,
          'email': testUser + '@vStock.io'
        }
      };

      request(options, function(err, res, body) {
        // if (err) console.log(err);
        assert(JSON.parse(body).success == true, "Create new user request failed");
        done();
      });

    });

    it("Performs authentication on user", function(done) {

      var headers = {};

      var options = {
        url: domain_url + 'authenticate',
        method: 'POST',
        headers: headers,
        form: {
          'username': testUser,
          'password': testUser
        }
      };

      request(options, function(err, res, body) {
          // if (err) console.log(err);
          assert(JSON.parse(body).success == true, "Authenticate request failed");
          token = JSON.parse(body).token;
          done();
      });

    });

    it("Sends GET request to get user data", function(done) {

      var headers = {
        'x-access-token': token
      };

      var options = {
        url: domain_url + 'users/' + testUser,
        method: 'GET',
        headers: headers,
        form: {}
      };

      request(options, function(err, res, body) {
        // if (err) console.log(err);
        assert(JSON.parse(body).username == testUser, "GET request shows wrong information or did not complete");
        done();
      });

    });

  });
});
