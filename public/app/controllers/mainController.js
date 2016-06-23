// TODO: import this into angular application and delete the local version of mainController created there

angular.module('mainController', [])

.controller('mainController', function($http, $location, Auth) {

  var vm = this;
  vm.titleMessage = 'Welcome to vStock!';

});
