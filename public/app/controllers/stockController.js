angular.module('stockController', [])

.controller('stockController', function($rootScope, $location, Stocks) {

  var vm = this;

  vm.buyStock = function() {

    Stocks.buyStock(vm.buy.ticker, vm.buy.quantity)
    .then(function(data) {
      vm.buydata = data.data;
      vm.buydata.ticker = vm.buy.ticker;
      delete vm.buy;
      $("#confirmBuyModal").modal('show');
    });

  };

  vm.confirmBuy = function() {

    Stocks.confirmBuyStock(vm.buydata.ticker, vm.buydata.amount)
    .success(function(data) {
      $("#confirmBuyModal").modal('hide');
    });

  };

  vm.cancelBuy = function() {
    $("#confirmBuyModal").modal('hide');
  };

  vm.sellStock = function() {

    Stocks.sellStock(vm.sell.ticker, vm.sell.quantity)
    .then(function(data) {
      vm.selldata = data.data;
      vm.selldata.ticker = vm.sell.ticker;
      delete vm.sell;
      $("#confirmSellModal").modal('show');
    });

  };

  vm.confirmSell = function() {

    Stocks.confirmSellStock(vm.selldata.ticker, vm.selldata.quantity)
    .success(function(data) {
      $("#confirmSellModal").modal('hide');
    });

  };

  vm.cancelBuy = function() {
    $("#confirmSellModal").modal('hide');
  };

});
