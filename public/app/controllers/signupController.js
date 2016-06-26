angular.module('signupController', [])

.controller('signupController', function(User, $location) {

  var vm = this;
  vm.titleMessage = 'Signup Page';

  vm.doSignUp = function() {
    vm.processing = true;
    vm.error = '';

    User.createUser(vm.signupData.username, vm.signupData.password, vm.signupData.email)
      .success(function(data) {
        vm.processing = false;

        if (data.success) {
          $location.path('/portfolio');
          console.log('You successfully signed up');
        } else {
          vm.error = data.message;
        }
      });
  }

});
