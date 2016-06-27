angular.module('authController', [])

.controller('authController', function($rootScope, $location, Auth) {

  var vm = this;

  vm.user = Auth.getUser();

});
