angular.module('adminService', [])

.factory('Admin', function('$http') {

  var adminFactory = {};

  // Use this service to get all users and their data
  adminFactory.getAllUsers = function() {
    return $http.get('/users');
  };

  // Use this to get user stats that will be logged for business analytics
  adminFactory.getUserStats = function() {
    return $http.get('/admin/users');
  };

  // Access user dashboard information - I'm still not sure what's gonna go here :P
  adminFactory.dashboard = function() {
    return $http.get('/admin');
  };

  return adminFactory;

});
