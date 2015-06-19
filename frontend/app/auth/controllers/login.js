'use strict';

angular.module('myApp.auth')

    .controller('LoginCtrl', ['$scope', 'User', '$location', function($scope, User, $location) {
        $scope.credentials = {};

        User.login($scope.credentials).then(function () {
            $location.path('food-trucks/:foodTruckId')
        })


    }]);
