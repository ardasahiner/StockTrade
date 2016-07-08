angular.module('stockController', [])

.controller('stockController', function($rootScope, $scope, $location, Stocks) {

  var vm = this;
  vm.processing = false;

  vm.getPortfolio = function() {
    Stocks.getPortfolio()
    .then(function(data) {
      vm.portfolio = data.data;
      console.log(vm.portfolio);
      $scope.portfolioAssets = vm.portfolio.assets;
    })
  }

  vm.getPortfolio();

  vm.buyStock = function() {

    vm.processing = true;

    Stocks.buyStock(vm.buy.ticker, vm.buy.quantity)
    .then(function(data) {
      vm.buydata = data.data;
      vm.buydata.ticker = vm.buy.ticker;
      delete vm.buy;
      vm.processing = false;
      console.log(vm.buydata);
      if (vm.buydata.success) {
        $("#buyModal").modal('hide');
        $("#confirmBuyModal").modal('show');
      }
    });

  };

  vm.confirmBuy = function() {

    vm.processing = true;

    Stocks.confirmBuyStock(vm.buydata.ticker, vm.buydata.amount)
    .success(function(data) {
      vm.processing = false;
      vm.getPortfolio();
      $("#confirmBuyModal").modal('hide');
    });

  };

  vm.cancelBuy = function() {
    vm.processing = false;
    delete vm.buydata;
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
      console.log(vm.selldata);
      if (vm.selldata.success) {
        $("#sellModal").modal('hide');
        $("#confirmSellModal").modal('show');
      }
    });

  };

  vm.confirmSell = function() {

    vm.processing = true;

    Stocks.confirmSellStock(vm.selldata.ticker, vm.selldata.quantity)
    .success(function(data) {
      vm.processing = false;
      vm.getPortfolio();
      $("#confirmSellModal").modal('hide');
    });

  };

  vm.cancelSell = function() {
    vm.processing = false;
    delete vm.selldata;
    $("#sellModal").modal('hide');
    $("#confirmSellModal").modal('hide');
  };

})

.directive('stockAsset', function() {
  return {
    restrict: 'E',
    scope: {
      info: '='
    },
    templateUrl: 'app/views/pages/authenticated/portfolioAsset.html'
  };
});
