app.config(function ($routeProvider) {
    "use strict";
    $routeProvider.when('/',
        {
            controller: 'HomeController',
            templateUrl: '/static/app/views/homepage.html'
        }).otherwise({redirectTo: '/'});
});