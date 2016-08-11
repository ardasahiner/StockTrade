angular.module('accountController', [])
  .controller('accountController', function($location, $window, User, Auth) {
    var vm = this;
    vm.loading = false;
    vm.currentActiveSort = "transactionDate";
    vm.currentSortOrientation = 1;
    // transactions controllers

    vm.getTransactions = function() {
      vm.loading = true;
      vm.currentActiveSort = "transactionDate";
      vm.currentSortOrientation = 1;
      Auth.getUser()
        .then(function(data) {
          vm.user = data.data;
          User.getTransactions(vm.user.username)
            .then(function(tData) {
              vm.transactionList = tData.data;
              console.log(vm.transactionList);
              vm.loading = false;
            })
            .catch(function(err) {
              vm.loading = false;
              console.log(err);
              console.log("Application Unavaliable");
              $location.path('/error');
            });
        })
        .catch(function(err) {
          vm.loading = false;
          console.log(err);
          console.log("Application Unavaliable");
          $location.path('/error');
        });
    }

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
    vm.getTransactions();

    vm.updateInfo = function() {
      vm.loading = true;
      vm.error = '';
      var userData = {};

      if (typeof vm.updateData == "undefined") {
        vm.error = "You must enter at least one field";
      } else if (typeof vm.updateData.password == "undefined"){
        vm.error = "You must enter your current password to make any changes.";
      } else {

        userData["password"] = vm.updateData.password;
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
        if (vm.updateData.newPassword !=  vm.updateData.confirmPassword) {
          vm.error = "Passwords do not match!";
        } else {
          if ((typeof vm.updateData.newPassword != "undefined" && vm.updateData.newPassword.length < 6) && vm.updateData.newPassword != "") {
              vm.error = "Password must be at least 6 characters";
          } else {
            if (typeof vm.updateData.newPassword != "undefined" && vm.updateData.newPassword != '' ) {

              userData["newPassword"] = vm.updateData.newPassword;
            }

            if (Object.keys(userData).length != 0) {
              // request
              console.log(userData);
              User.updateUser(vm.user.username, userData)
                .success(function(data) {
                  vm.loading = false;
                  if (data.success) {
                    $window.location.reload();
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
