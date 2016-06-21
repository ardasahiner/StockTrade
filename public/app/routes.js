angular.module('routerRoutes', ['ngRoute'])

.config(function($routeProvider, $locationProvider) {
  $routeProvider

    .when('/', {
      templateUrl: 'app/views/pages/unauthenticated/home.html',
      controller: 'homeController',
      controllerAs: 'home'
    })

    .when('/about', {
      templateUrl: 'app/views/pages/unauthenticated/aboutus.html',
      controller: 'aboutController',
      controllerAs: 'about'
    })

    .when('/contact', {
      templateUrl: 'app/views/pages/unauthenticated/contactus.html',
      controller: 'contactController',
      controllerAs: 'contact'
    })

    .when('/login', {
      templateUrl: 'app/views/pages/unauthenticated/login.html',
      controller: 'loginController',
      controllerAs: 'login'
    })

    .when('/signup', {
      templateUrl: 'app/views/pages/unauthenticated/signup.html',
      controller: 'signupController',
      controllerAs: 'signup'
    })

    .when('/terms', {
      templateUrl: 'app/views/pages/unauthenticated/termsofuse.html',
      controller: 'termsofuseController',
      controllerAs: 'termsofuse'
    });

  $locationProvider.html5Mode(true);
});
