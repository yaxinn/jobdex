app.controller('mainCtrl', function ($scope, $http, $cookies) {
    $scope.title = "Jobdex";
});

function error(xhr, ajaxOptions, thrownError) {
    console.log(xhr.responseText);
}


