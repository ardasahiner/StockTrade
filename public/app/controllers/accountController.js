angular.module('accountController', ['ui.bootstrap'])
  .controller('accountController', function($location, User, Auth) {
    var vm = this;
    vm.updateData = {};
    vm.loading = false;

    vm.getInfo = function() {
      vm.loading = true;
      Auth.getUser()
        .then(function(data) {
          vm.user = data.data;
          console.log(vm.user);
          vm.updateData.firstName = vm.user.firstName;
          vm.updateData.lastName = vm.user.lastName;
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
        if (typeof vm.updateData.firstName != "undefined" && vm.updateData.firstName != vm.user.firstName) {
          console.log(vm.user.firstName);
          userData["firstName"] = vm.updateData.firstName;
        }
        if (typeof vm.updateData.lastName != "undefined" && vm.updateData.lastName != vm.user.lastName) {
          userData["lastName"] = vm.updateData.lastName;
        }
        if (typeof vm.updateData.botAccount != "undefined" && vm.updateData.botAccount != vm.user.botAccount) {
          userData["botAccount"] = vm.updateData.botAccount;
        }
        if (vm.updateData.password !=  vm.updateData.confirmPassword) {
          vm.error = "Passwords do not match!";
        } else {
          if ((typeof vm.updateData.password != "undefined" && vm.updateData.password.length < 6) && vm.updateData.password != "") {
              console.log(vm.updateData.password);
              vm.error = "Password must be at least 6 characters";
          } else {
            if (typeof vm.updateData.password != "undefined" && vm.updateData.password != '' ) {

              userData["password"] = vm.updateData.password;
            }

            if (Object.keys(userData).length != 0) {
              // request
              console.log(userData);
              User.updateUser(vm.user.username, userData)
                .success(function(data) {
                  vm.loading = false;
                  if (data.success) {
                    console.log(data.success);
                    $location.path('/account');
                  } else {
                    vm.error = data.message;
                  }
               });

            } else {

              vm.error = "You must enter at least one field";
            }
          }
        }
      }
      vm.loading = false;
    };
  });
