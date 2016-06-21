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
    });

  $locationProvider.html5Mode(true);
});
