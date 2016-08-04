angular.module('mainController', [])

.controller('mainController', function($rootScope, $scope, $location, $state, Auth, $anchorScroll) {

  var vm = this;

  // Get info about whether user is logged in
  vm.loggedIn = Auth.isLoggedIn();
  $scope.state = $state;

  // Check every request to see if user is logged in
  // This function runs everytime there is a state change
  $rootScope.$on('$stateChangeStart', function(toState) {
    vm.loggedIn = Auth.isLoggedIn();

    Auth.getUser()
      .then(function(data) {
        vm.user = data.data;
      })
      $anchorScroll();
  });

  // Function to handle login requests
  vm.doLogin = function() {
    vm.processing = true;
    vm.error = '';

    Auth.login(vm.loginData.username, vm.loginData.password)
    .success(function(data) {
      vm.processing = false;

      // If successful authentication, user is redirected to their portfolio
      if (data.success) {
        $location.path('/portfolio');
        $("#loginModal").modal('hide');
      } else {
        vm.error = data.message;
      }
    });
  };

  // Function to handle logout requests
  vm.doLogout = function() {
    Auth.logout();
    vm.user = '';
    vm.loggedIn = false;

    $location.path('/');
  };

});
