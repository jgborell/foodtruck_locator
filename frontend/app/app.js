'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
    'ngRoute',
    'myApp.foodTruckList',
    'myApp.foodTruckDetail',
    'myApp.addFoodTruck',
    'myApp.view2',
    'myApp.version',
    'restangular'
]).
    config(['$routeProvider', 'RestangularProvider', function ($routeProvider, RestangularProvider) {
        $routeProvider.otherwise({redirectTo: '/food-trucks'});
        RestangularProvider.setBaseUrl('http://localhost:8001');
        RestangularProvider.setRequestSuffix('/');

    }])
.controller('AppCtrl', function ($scope, Restangular) {

    });