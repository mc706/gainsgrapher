app.service('EmbeddedService', [
    "$http",
    "$q",
    function ($http, $q) {
        'use strict';
        return {
            getObjectFromUrl: function (url, cache) {
                var defer = $q.defer();
                $http({
                    method: "GET",
                    cache: cache,
                    url: url
                }).success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
                return defer.promise;
            },
            postObjectToUrl: function (url, data) {
                var defer = $q.defer();
                $http({
                    method: "POST",
                    data: data,
                    url: url
                }).success(function (data, status, headers, config) {
                    defer.resolve(data);
                }).error(function (data, status, headers, config) {
                    defer.reject(status);
                });
                return defer.promise;
            }
        };
    }]);