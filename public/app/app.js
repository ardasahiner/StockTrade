// Add all modules to import list
var imports = [];
imports.push('app.routes');
imports.push('userService', 'stockService', 'adminService', 'authService');
imports.push('mainController', 'signupController', 'stockController', "searchController");

angular.module('vStockApp', imports)

// Custom configuration to get rid of # prefix on URLs
.config(function($httpProvider, $uiViewScrollProvider) {
  $httpProvider.interceptors.push('AuthInterceptor');
  $uiViewScrollProvider.useAnchorScroll();
})

// This function listens for all state changes
// If user tries to visit authenticated pages while not logged in,
//    user will be redirected to log in page
.run(['$rootScope', '$location', 'Auth',
function ($rootScope, $location, Auth) {

  $rootScope.$on('$stateChangeStart', function (event, toState, fromState) {

    if (toState.authenticated && !Auth.isLoggedIn()) {
      $location.path('/');
    }

  });

}]);
