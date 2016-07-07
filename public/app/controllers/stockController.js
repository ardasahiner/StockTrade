angular.module('stockController', [])

.controller('stockController', function($rootScope, $location, Stocks) {

  var vm = this;
  vm.processing = false;

  vm.buyStock = function() {

    vm.processing = true;

    Stocks.buyStock(vm.buy.ticker, vm.buy.quantity)
    .then(function(data) {
      vm.buydata = data.data;
      vm.buydata.ticker = vm.buy.ticker;
      delete vm.buy;
      vm.processing = false;
      $("#buyModal").modal('hide');
      $("#confirmBuyModal").modal('show');
    });

  };

  vm.confirmBuy = function() {

    vm.processing = true;

    Stocks.confirmBuyStock(vm.buydata.ticker, vm.buydata.amount)
    .success(function(data) {
      vm.processing = false;
      $("#confirmBuyModal").modal('hide');
    });

  };

  vm.cancelBuy = function() {
    vm.processing = false;
    $("#buyModal").modal('hide');
    $("#confirmBuyModal").modal('hide');
  };

  vm.sellStock = function() {

    vm.processing = true;

    Stocks.sellStock(vm.sell.ticker, vm.sell.quantity)
    .then(function(data) {
      vm.selldata = data.data;
      vm.selldata.ticker = vm.sell.ticker;
      delete vm.sell;
      vm.processing = false;
      $("#sellModal").modal('hide');
      $("#confirmSellModal").modal('show');
    });

  };

  vm.confirmSell = function() {

    vm.processing = true;

    Stocks.confirmSellStock(vm.selldata.ticker, vm.selldata.quantity)
    .success(function(data) {
      vm.processing = false;
      $("#confirmSellModal").modal('hide');
    });

  };

  vm.cancelSell = function() {
    vm.processing = false;
    $("#sellModal").modal('hide');
    $("#confirmSellModal").modal('hide');
  };

});
