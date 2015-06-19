'use strict';

angular.module('myApp.foodTruckDetail', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/food-trucks/:foodTruckId', {
            templateUrl: 'food_truck_detail/food-truck-detail.html',
            controller: 'FoodTruckDetailCtrl'
        });
    }])

    .controller('FoodTruckDetailCtrl', ['$scope', '$routeParams', '$location', 'Restangular', function ($scope,
                                                                                                      $routeParams, $location, Restangular) {
        $scope.foodTruckId = $routeParams.foodTruckId;

        Restangular.one('food-trucks', $scope.foodTruckId).customGET()
            .then(
            function (foodTruck) {
                $scope.foodTruck = foodTruck;
            },
            function () {
                alert("There appears to be a problem ¯\_(ツ)_/¯");
            }
        );
        $scope.deleteFoodTruck = function () {
            var confirmation = confirm("Are you sure you want to remove this Food Truck from your account? This can not be undone.");

            if (confirmation) {
                Restangular.one('food-trucks', $scope.foodTruckId).customDELETE()
                    .then(
                    function () {
                        alert("Your Food Truck was successfully deleted!");
                        $location.path('/food-trucks');
                    },
                    function () {
                        alert("Unable to delete your Food Truck ¯\_(ツ)_/¯");
                    })
            }
        };
        $scope.SaveEditedFoodTruck = function () {
            Restangular.one('food-trucks', $scope.foodTruckId).customPUT($scope.foodTruck)
                .then(
                    function () {
                        alert("Your food truck was successfully updated");
                    },
                    function () {
                        alert("Unable to edit/update your Food Truck ¯\_(ツ)_/¯");
                    }
            )
        }

}]);
