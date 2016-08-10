angular.module('userService', [])

.factory('User', function($http, AuthToken) {

  var userFactory = {};

  // Get a single user by username
  userFactory.get = function(username) {
    return $http.get('/users/' + username);
  };

  // // Get all users
  // userFactory.getAll = function() {
  //   return $http.get('/users');
  // }

  // Create a new user
  userFactory.createUser = function(username, password,
    firstname, lastname, email, bot) {
      return $http.post('/users/', {
        username: username,
        firstName: firstname,
        lastName: lastname,
        password: password,
        email: email,
        bot: bot
      });
    };

    // Update an existing user's data
    userFactory.updateUser = function(username, userData) {
      return $http.put('/users/' + username, userData)
      .success(function(data) {
        AuthToken.setToken(data.token);
        return data;
      });
    };

    // Delete an existing user
    userFactory.deleteUser = function(username) {
      return $http.delete('/users/' + username);
    };

    return userFactory;

  });
