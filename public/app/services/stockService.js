angular.module('stockService', [])

.factory('Stocks', function($http) {

  var stockFactory = {};

  stockFactory.getPrice = function(stock_symbol) {
    return $http.get('/stocks/' + stock_symbol);
  };

  return stockFactory;

});
