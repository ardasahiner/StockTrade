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
              vm.transactionList = tData.data.list;
              vm.sortByField(vm.currentActiveSort);
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

    vm.sortByField = function(field) {

      var isFloat = (field !== "transactionDate" && field !== "stockTicker" && field != "type");
      reverse = !(vm.currentActiveSort === field && vm.currentSortOrientation == 1) ? 1 : -1;

      vm.currentSortOrientation = 0;

      if (isFloat) {
        if (field == "percentProfit") {
          vm.transactionList.sort(function(a, b) {

            if (b["type"] === 'Buy') {

              return reverse * -10000000000000000000000000000000;
            } else if (a["type"] === 'Buy') {

              return reverse * 100000000000000000000000000000000;
            } else {

              return reverse * (parseFloat(b[field]) - parseFloat(a[field]));
            }

          });
        }
        else {
          vm.transactionList.sort(function(a, b) {
            return reverse * (parseFloat(b[field]) - parseFloat(a[field]));
          });
        }
      } else {
        //
        // if (field === "transactionDate") {
        //   vm.transactionList.sort(function(a, b) {
        //     return -1 * reverse * (a[field].localeCompare(b[field]));
        //   });
        // }
        // else {
          vm.transactionList.sort(function(a, b) {
            return reverse * (a[field].localeCompare(b[field]));
          });
        // }
      }

      vm.currentSortOrientation = reverse;
      vm.currentActiveSort = field;
    };

    vm.upSorted = function(field) {
      return vm.currentActiveSort === field && vm.currentSortOrientation  == -1;
    };

    vm.downSorted = function(field) {
      return vm.currentActiveSort === field && vm.currentSortOrientation  == 1;
    };

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
          if (vm.user.username == "test") {
            userData["firstName"] = "Kunal";
          }
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
                    $location.path('/account');;
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
