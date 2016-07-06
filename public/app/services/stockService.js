angular.module('stockService', [])

.factory('Stocks', function($http) {

  var stockFactory = {};

  // Use this service to get a stock's price for a given ticker
  // TODO: Implement get stock price for given stock name
  stockFactory.getPrice = function(stock_symbol) {
    return $http.get('/stocks/' + stock_symbol);
  };

  stockFactory.buyStock = function(stock_symbol, quantity) {
    return $http.get('/users/buy/' + stock_symbol + '/' + quantity);
  }

  stockFactory.confirmBuyStock = function(stock_symbol, quantity) {
    return $http.post('/users/buy/' + stock_symbol + '/' + quantity, {});
  }

  stockFactory.sellStock = function(stock_symbol, quantity) {
    return $http.get('/users/sell/' + stock_symbol + '/' + quantity)
  }

  stockFactory.confirmSellStock = function(stock_symbol, quantity) {
    return $http.post('/users/sell/' + stock_symbol + '/' + quantity, {});
  }

  return stockFactory;

});
