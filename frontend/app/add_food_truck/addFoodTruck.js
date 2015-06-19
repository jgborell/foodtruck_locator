'use strict';

angular.module('myApp.addFoodTruck', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/add-food-truck', {
            templateUrl: 'add_food_truck/add-food-truck.html',
            controller: 'addFoodTruckCtrl'
        });
    }])

    .controller('addFoodTruckCtrl', ['$scope', 'Restangular', '$location', function ($scope, Restangular, $location) {
        $scope.foodTruck = {};

        $scope.addFoodTruck = function () {
            Restangular.all('add-food-truck').customPOST($scope.foodTruck)
                .then(
                    function () {
                        alert("Food Truck was created successfully!");
                        $scope.foodTruck = {};
                        $location.path('/food-trucks/:foodTruckId');
                    },
                    function () {
                        alert("Unable to create your Food Truck ¯\_(ツ)_/¯");
                    });
                };
            }]);