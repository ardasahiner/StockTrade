angular.module('stockController', [])

.controller('stockController', function($rootScope, $location, Stocks) {

  var vm = this;
  vm.currentBuy = false;
  vm.currentSell = false;

  vm.buyStock = function() {

    Stocks.buyStock(vm.buy.ticker, vm.buy.quantity)
    .then(function(data) {
      vm.buydata = data.data;
      vm.buydata.ticker = vm.buy.ticker;
      vm.currentBuy = true;
      delete vm.buy;
      console.log(vm.buydata);
    });
  };

  vm.confirmBuy = function() {

    Stocks.confirmBuyStock(vm.buydata.ticker, vm.buydata.amount)
    .success(function(data) {
      console.log(data);
      vm.currentBuy = false;
    });
  };

  vm.cancelBuy = function() {
    vm.currentBuy = false;
  };

  vm.sellStock = function() {

    Stocks.sellStock(vm.sell.ticker, vm.sell.quantity)
    .then(function(data) {
      vm.selldata = data.data;
      vm.selldata.ticker = vm.sell.ticker;
      vm.currentSell = true;
      delete vm.sell;
      console.log(data);
    });
  };

  vm.confirmSell = function() {

    Stocks.confirmSellStock(vm.selldata.ticker, vm.selldata.quantity)
    .success(function(data) {
      console.log(data.data);
      vm.currentSell = false;
    });
  };

  vm.cancelBuy = function() {
    vm.currentSell = false;
  };

});
