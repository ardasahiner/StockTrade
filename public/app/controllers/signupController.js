angular.module('signupController', [])

.controller('signupController', function(User, Auth, $location) {

  var vm = this;
  vm.titleMessage = 'Signup Page';

  vm.doSignUp = function() {
    vm.processing = true;
    vm.error = '';

    if (vm.signupData.password != vm.signupData.confirmpassword) {
      vm.error = "Passwords don't match!";
    } else {

      User.createUser(vm.signupData.username, vm.signupData.password,
        vm.signupData.firstname, vm.signupData.lastname, vm.signupData.email, vm.signupData.bot)

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
            console.log(vm.error);
          }
        });
      }
    }

  });
