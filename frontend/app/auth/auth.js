'use strict';

angular.module('myApp.auth', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/login', {
            templateUrl: 'auth/templates/login.html',
            controller: 'LoginCtrl'
        });
    }]);

