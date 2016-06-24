// Add all modules to import list
var imports = [];
imports.push('app.routes');
imports.push('userService', 'stockService', 'adminService');
imports.push('mainController', 'aboutController', 'contactController',
  'homeController', 'loginController', 'signupController', 'termsofuseController');

angular.module('vStockApp', imports);
