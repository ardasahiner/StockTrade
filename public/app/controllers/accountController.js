angular.module('accountController', ['ui.bootstrap'])
  .controller('accountController', function($location, User, Auth) {
    var vm = this;
    vm.loading = false;

    vm.getInfo = function() {
      vm.loading = true;
      Auth.getUser()
        .then(function(data) {
          vm.user = data.data;
          vm.loading = false;
        })
        .catch(function(err) {
          vm.loading = false;
          console.log(err);
          console.log("Application Unavaliable");
          $location.path('/error');
        });
    };
    vm.getInfo();

    vm.updateInfo = function() {
      vm.loading = true;
      vm.error = '';
      var userData = {};

      if (typeof vm.updateData == "undefined") {
        vm.error = "You must enter at least one field";
      } else {
        if (typeof vm.updateData.firstName != "undefined") {
          userData["firstName"] = vm.updateData.firstName;
        }
        if (typeof vm.updateData.lastName != "undefined") {
          userData["lastName"] = vm.updateData.lastName;
        }
        if (typeof vm.updateData.botAccount != "undefined") {
          userData["botAccount"] = vm.updateData.botAccount;
        }
        if (vm.updateData.password !=  vm.updateData.confirmPassword) {
          vm.error = "Passwords do not match!";
        } else {
          if (typeof vm.updateData.password != "undefined" && vm.updateData.password.length < 6) {
              vm.error = "Password must be at least 6 characters";
          } else {
            if (typeof vm.updateData.password != "undefined") {

              userData["password"] = vm.updateData.password;
            }
            // request
            console.log(userData);
            // User.updateUser(vm.user.username, userData)
            //   .success(function(data) {
            //     vm.loading = false;
            //     if (data.success) {
            //       $location.path('/account');
            //     } else {
            //       vm.error = data.message;
            //   });
          }
        }
      }


      // if (vm.updateData.password != vm.updateData.confirmPassword) {
      //   vm.error = "Passwords don't match!";
      // } else if (vm.upateData.newPassword.length < 6) {
      //   vm.error = "Password must be longer than 6 characters";
      // }

    };
  });
