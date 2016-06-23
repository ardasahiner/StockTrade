angular.module('stockService', [])

.factory('Stocks', function($http) {

  var stockFactory = {};

  // Use this service to get a stock's price for a given ticker
  // TODO: Implement get stock price for given stock name
  stockFactory.getPrice = function(stock_symbol) {
    return $http.get('/stocks/' + stock_symbol);
  };

  return stockFactory;

});
