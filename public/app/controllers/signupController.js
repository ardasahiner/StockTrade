angular.module('signupController', [])

.controller('signupController', function(User, Auth, $location) {

  var vm = this;
  vm.titleMessage = 'Signup Page';

  vm.doSignUp = function() {
    vm.processing = true;
    vm.error = '';

    User.createUser(vm.signupData)
      .success(function(data) {

        if (data.success) {

          Auth.login(vm.signupData.username, vm.signupData.password)
            .success(function(data) {
              vm.processing = false;

              if (data.success) {
                $location.path('/portfolio');
                console.log('You successfully signed up');
              } else {
                vm.error = data.message;
              }
            });

        } else {
          vm.error = data.message;
        }
      });
  }

});
