// Add all modules to import list
var imports = [];
imports.push('app.routes');
imports.push('adminService', 'stockService', 'userService');
imports.push('mainController');

angular.module('vStockApp', imports)

.controller('homeController', function() {
  var vm = this;
  vm.titleMessage = 'Welcome to the home page of vStock';
})

.controller('aboutController', function() {
  var vm = this;
  vm.titleMessage = 'This is the about page';
})

.controller('contactController', function() {
  var vm = this;
  vm.titleMessage = 'Contact Us!';
})

.controller('loginController', function() {
  var vm = this;
  vm.titleMessage = 'Log in here!';
})

.controller('signupController', function() {
  var vm = this;
  vm.titleMessage = 'Sign up here!';
})

.controller('termofuseController', function() {
  var vm = this;
  vm.titleMessage = 'These are the terms of use';
});
