
app.controller('businessManagement.ecommerce.todo' , function($scope , $http , $aside , $state, $Flash , $users , $filter , $permissions , $sce){

  // $http.get('/api/ecommerce/todo/').then()

$scope.data={
  name:'',

}
$scope.press = function(){
  console.log($scope.data,"noooooooo");
  $http({
    method: 'POST',
    url: '/api/ecommerce/todo/',
    data: $scope.data

  }).then (function(response){
    console.log(response.status);
  });
}
});
