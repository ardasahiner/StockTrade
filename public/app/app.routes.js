angular.module('app.routes', ['ui.router'])

.config(function($stateProvider, $urlRouterProvider) {

  $urlRouterProvider.otherwise('/404');

  $stateProvider

    .state('home', {
      url: '/',
      templateUrl: 'app/views/pages/unauthenticated/home.html'
    })

    .state('about', {
      url: '/about',
      templateUrl: 'app/views/pages/unauthenticated/aboutus.html',
      controller: 'aboutController',
      controllerAs: 'about'
    })

    .state('contact', {
      url: '/contact',
      templateUrl: 'app/views/pages/unauthenticated/contactus.html',
      controller: 'contactController',
      controllerAs: 'contact'
    })

    .state('login', {
      url: '/login',
      templateUrl: 'app/views/pages/unauthenticated/login.html',
      controller: 'loginController',
      controllerAs: 'login'
    })

    .state('signup', {
      url: '/signup',
      templateUrl: 'app/views/pages/unauthenticated/signup.html',
      controller: 'signupController',
      controllerAs: 'signup'
    })

    .state('terms', {
      url: '/terms',
      templateUrl: 'app/views/pages/unauthenticated/termsofuse.html',
      controller: 'termsofuseController',
      controllerAs: 'termsofuse'
    })

    .state('404', {
      url: '/404',
      templateUrl: 'app/views/pages/404.html',
    });

})

.config(["$locationProvider", function($locationProvider) {
  $locationProvider.html5Mode(true);
}]);
