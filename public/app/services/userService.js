angular.module('userService', [])

.factory('User', function($http) {

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
  userFactory.createUser = function(userData) {
    return $http.post('/users/', userData);
  };

  // Update an existing user's data
  userFactory.updateUser = function(username, userData) {
    return $http.put('/users/' + username, userData);
  };

  // Delete an existing user
  userFactory.deleteUser = function(username) {
    return $http.delete('/users/' + username);
  };

  return userFactory;

});
