angular.module('myApp.auth')

    .service('User', ['Restangular', function(Restangular) {
        this.info = {};

        this.login = function(credentials) {
            var that = this;
            return Restangular.one('login').customPOST(credentials).then(function (data) {
                that.info = data
            })

        }
    }]);
