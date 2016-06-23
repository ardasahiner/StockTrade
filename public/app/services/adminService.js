angular.module('adminService', [])

.factory('Admin', function('$http') {

  var adminFactory = {};

  adminFactory.getAllUsers = function() {
    return $http.get('/users');
  };

  adminFactory.getUserStats = function() {
    return $http.get('/admin/users');
  };

  adminFactory.dashboard = function() {
    return $http.get('/admin');
  };

  return adminFactory;

});
