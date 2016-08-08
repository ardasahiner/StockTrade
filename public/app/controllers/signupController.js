angular.module('signupController', [])

.controller('signupController', function(User, Auth, $location, $anchorScroll) {

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

          console.log(data);

          if (data.success) {

            Auth.login(vm.signupData.username, vm.signupData.password)
            .success(function(data) {
              vm.processing = false;

              if (data.success) {
                delete vm.signupData;
                $location.path('/portfolio');
                $("#signupModal").modal('hide');
                $anchorScroll();
              } else {
                vm.error = data.message;
              }
            });

          } else {
            vm.error = data.message;
            if (data.message.errmsg.includes("duplicate key error") && data.message.errmsg.includes("$username")) {
              vm.error = "Username: " + data.message.op.username + " is taken!";
            }
            if (data.message.errmsg.includes("duplicate key error") && data.message.errmsg.includes("$email")) {
              vm.error = "Email: " + data.message.op.email + " is taken!";
            }
          }
        });
      }
    }

  });
