angular.module('stockService', [])

.factory('Stocks', function($http) {

  var stockFactory = {};

  // Use this service to get a stock's price for a given ticker
  stockFactory.getPrice = function(stock_symbol) {
    return $http.get('/stocks/' + stock_symbol);
  };

  stockFactory.historicData = function(stock_symbol) {
    return $http.get('https://www.quandl.com/api/v3/datasets/WIKI/' + stock_symbol + '.json?api_key=YxZtiPjFd-mjcJbaTUvd');
  };

  stockFactory.buyStock = function(stock_symbol, quantity) {
    return $http.get('/users/buy/' + stock_symbol + '/' + quantity);
  };

  stockFactory.confirmBuyStock = function(stock_symbol, quantity) {
    return $http.post('/users/buy/' + stock_symbol + '/' + quantity, {});
  };

  stockFactory.sellStock = function(stock_symbol, quantity) {
    return $http.get('/users/sell/' + stock_symbol + '/' + quantity)
  };

  stockFactory.confirmSellStock = function(stock_symbol, quantity) {
    return $http.post('/users/sell/' + stock_symbol + '/' + quantity, {});
  };

  stockFactory.getPortfolio = function() {
    return $http.get('/users/portfolio');
  };

  return stockFactory;

});
