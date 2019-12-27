app.controller('businessManagement.ecommerce.client' , function($scope , $http , $aside , $state, Flash , $users , $filter , $permissions , $sce){

$scope.data={
  email:'',
  mobile:'',
  message:'',
}
$scope.submit = function(){
  console.log($scope.data,"sadddddddd");
  $http({
    method: 'POST',
    url: '/api/ecommerce/feedback/',
    data: $scope.data

  }).then (function(response){
    console.log(response.status);
  });
}
});
