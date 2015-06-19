'use strict';

angular.module('myApp.foodTruckList', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/food-trucks', {
            templateUrl: 'food_truck_list/food-truck-list.html',
            controller: 'foodTruckListCtrl'
        });
    }])

    .controller('foodTruckListCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
        Restangular.all('food-trucks').getList().then(function (foodTruckList) {
            $scope.foodTruckList = foodTruckList;
        })
    }]);