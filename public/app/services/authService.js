angular.module('authService', [])

.factory('Auth', function($http, $q, AuthToken) {
  var authFactory = {};

  // Login and set Token
  authFactory.login = function(username, password, rememberMe) {
    return $http.post('/authenticate', {
      username: username,
      password: password,
      rememberMe: rememberMe
    })
    .success(function(data) {
      AuthToken.setToken(data.token);
      return data;
    });
  };

  // Logout and clear the token
  authFactory.logout = function() {
    AuthToken.setToken();
  };

  // Check if user is logged in
  authFactory.isLoggedIn = function() {
    if (AuthToken.getToken()) {
      return true;
    } else {
      return false;
    }
  };

  // Get user info for logged in user
  authFactory.getUser = function() {
    if (AuthToken.getToken()) {
      return $http.get('/users/me');
    } else {
      AuthToken.setToken();
      return $q.reject({ message: 'You need a token to cross the bridge' });
    }
  };

  return authFactory;
})

.factory('AuthToken', function($window) {
  var authTokenFactory = {};

  // Get the token from local storage in browser
  authTokenFactory.getToken = function() {
    return $window.localStorage.getItem('token');
  };

  // Set the token or clear the token
  authTokenFactory.setToken = function(token) {
    if (token) {
      $window.localStorage.setItem('token', token);
    } else {
      $window.localStorage.removeItem('token');
    }
  };

  return authTokenFactory;
})

.factory('AuthInterceptor', function($q, AuthToken, $location) {
  var AuthInterceptorFactory = {};

  // Attach the token to every request
  AuthInterceptorFactory.request = function(config) {
    var token = AuthToken.getToken();

    if (token) {
      config.headers['x-access-token'] = token;
    }

    return config;
  };

  // Redirect if a token doesnt authenticate or no token
  AuthInterceptorFactory.responseError = function(res) {
    if (res.status == 403) {
      AuthToken.setToken();
      $("#loginModal").modal('show');
    }
    return $q.reject(res);
  };

  return AuthInterceptorFactory;
});
