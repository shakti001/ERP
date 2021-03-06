app.config(function($stateProvider) {

  $stateProvider
    .state('workforceManagement.recruitment.jobs', {
      url: "/jobs",
      views: {
        "": {
          templateUrl: '/static/ngTemplates/app.recruitment.jobs.html',
          controller: 'workforceManagement.recruitment.jobs',
        }
      }
    })
});
app.controller("workforceManagement.recruitment.jobs", function($scope, $http, $uibModal,$aside, $state, Flash, $users, $filter, $permissions) {

  $scope.data = {
    tableData: []
  };

  views = [{
    name: 'list',
    icon: 'fa-th-large',
    template: '/static/ngTemplates/genericTable/genericSearchList.html',
    itemTemplate: '/static/ngTemplates/app.recruitment.jobs.item.html',
  }, ];


  $scope.config = {
    views: views,
    url: '/api/recruitment/jobs/',
    searchField: 'jobtype',
    itemsNumPerView: [16, 32, 48],
  }

  $scope.tableAction = function(target, action, mode) {
    console.log(target, action, mode);
    console.log("fdg",$scope.data.tableData);

    for (var i = 0; i < $scope.data.tableData.length; i++) {
      if ($scope.data.tableData[i].pk == parseInt(target)) {
        if (action == 'edit') {
          var title = 'Edit Jobs: ';
          var myapp = 'jobEdit';
        } else if (action == 'jobBrowse') {
          var title = 'Browse Jobs : ';
          var myapp = 'jobBrowse';
        }
        $scope.addTab({
          title: title + $scope.data.tableData[i].pk,
          cancel: true,
          app: myapp,
          data: {
            pk: target,
            index: i
          },
          active: true
        })
      }
    }

  }
  $scope.tabs = [];
  $scope.searchTabActive = true;
  $scope.closeTab = function(index) {
  $scope.tabs.splice(index, 1)
}

$scope.addTab = function(input) {
  console.log(JSON.stringify(input));
  $scope.searchTabActive = false;
  alreadyOpen = false;
  console.log($scope.tabs,$scope.tabs.length);
  for (var i = 0; i < $scope.tabs.length; i++) {
    console.log('***********************');
    if ($scope.tabs[i].data.pk == input.data.pk && $scope.tabs[i].app == input.app) {
      $scope.tabs[i].active = true;
      alreadyOpen = true;
    } else {
      $scope.tabs[i].active = false;
    }
  }
  if (!alreadyOpen) {
    console.log(input);
    $scope.tabs.push(input)
    console.log($scope.tabs,$scope.tabs.length);
  }
}
});
app.controller("workforceManagement.recruitment.roles.form", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {

  $scope.refreshOption = true;
  $scope.departmentSearch = function(query) {
    return $http.get('/api/organization/departments/?dept_name__contains=' + query).
    then(function(response) {
      return response.data;
    })
  };
  $scope.unitsSearch = function(query) {
    return $http.get('/api/organization/units/?name__contains=' + query).
    then(function(response) {
      return response.data;
    })
  };
  $scope.roleSearch = function(query) {
    return $http.get('/api/organization/roles/?name__contains=' + query).
    then(function(response) {
      return response.data;
    })
  };
  $scope.resetForm =function(){
  $scope.form = {
    'jobtype': '',
    'unit': '',
    'department': '',
    'role': '',
    'contacts': [],
    'skill': '',
  }
  }

  if (typeof $scope.tab != 'undefined' && $scope.tab.data.pk != -1) {
  if ($scope.tab.data.index == undefined) {
    $scope.form = $scope.tab.data.jObData;
  }else {
    $scope.form = $scope.data.tableData[$scope.tab.data.index];
  }
  $scope.mode = 'edit';
  console.log($scope.form)
} else {
  $scope.resetForm();
}

  $scope.saveJobs = function() {
    var f = $scope.form;
    var toSend = {
      jobtype: f.jobtype,
      unit: f.unit.pk,
      department: f.department.pk,
      role: f.role.pk,
      contacts: f.contacts,
      skill: f.skill
    }
    console.log(toSend);
    var url = '/api/recruitment/jobs/';
    if ($scope.form.pk == undefined) {
      var method = 'POST';
    } else {
      var method = 'PATCH';
      url += $scope.form.pk + '/';
    }
    $http({
      method: method,
      url: url,
      data: toSend
    }).
    then(function(response) {
      // $scope.form= response.data;
      Flash.create('success', 'Saved');
    })
  }

});
app.controller("workforceManagement.recruitment.jobs.explore", function($scope, $state, $users, $stateParams, $http, Flash, $uibModal) {

  $scope.jobDetails = $scope.data.tableData[$scope.tab.data.index]

  });
