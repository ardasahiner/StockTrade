angular.module('stockController', [])

.controller('stockController', function($rootScope, $location, Stocks) {

  var vm = this;
  vm.currentBuy = false;

  vm.buyStock = function() {

    Stocks.buyStock(vm.buy.ticker, vm.buy.quantity)
      .then(function(data) {
        vm.buydata = data.data;
        vm.buydata.ticker = vm.buy.ticker;
        vm.currentBuy = true;
        console.log(vm.buydata);
      });
  };

  vm.confirmBuy = function() {

    Stocks.confirmBuyStock(vm.buy.ticker, vm.buy.quantity)
      .success(function(data) {
        console.log(data);
        vm.currentBuy = false;
      });
  };

  vm.sellStock = function() {

    Stocks.sellStock(vm.sell.ticker, vm.sell.quantity)
      .then(function(data) {
        console.log(data);
      });
  };

});
