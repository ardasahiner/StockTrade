angular.module('stockController', [])

.controller('stockController', function($rootScope, $location, $state, Stocks) {

  var vm = this;

  vm.buyStock = function() {

    Stocks.buyStock(vm.buy.ticker, vm.buy.quantity)
      .then(function(data) {
        console.log(data);
      });
  };

  vm.sellStock = function() {

    Stocks.sellStock(vm.sell.ticker, vm.sell.quantity)
      .then(function(data) {
        console.log(data);
      });
  };

});
