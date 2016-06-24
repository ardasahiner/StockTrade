angular.module('mainController', [])

.controller('mainController', function($rootScope, $location, Auth) {

  var vm = this;

  // Get info about whether user is logged in
  vm.loggedIn = Auth.isLoggedIn();

  // Check every request to see if user is logged in
  $rootScope.$on('$routeChangeStart', function() {
    vm.loggedIn = Auth.isLoggedIn();

    Auth.getUser()
      .then(function(data) {
        vm.user = data.data;
      });
  });

  // Function to handle login requests
  vm.doLogin = function() {
    vm.processing = true;
    vm.error = '';

    Auth.login(vm.loginData.username, vm.loginData.password)
      .success(function(data) {
        vm.processing = false;

        if (data.success) {
          $location.path('/portfolio');
          console.log('You successfully logged in');
        } else {
          vm.error = data.message;
        }
      });
  };

  // Function to handle logout requests
  vm.doLogout = function() {
    Auth.logout();
    vm.user = '';

    $location.path('/');
  };

});
