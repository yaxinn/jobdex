'use strict';

var app = angular.module('jobdex_app', ['ngCookies']);

app.controller('UserController', function($scope, $http) {
	this.user = {};

	this.sign_up = function(){		
		//Modeled off of http://tutorials.jenkov.com/angularjs/ajax.html
		$scope.myData = JSON.stringify({user: this.user.username, password: this.user.password, email: this.user.email});
		
		var responsePromise = $http.post(dummyURL.herokuapp.com/UserModel/sign_up, $scope.myData);

		responsePromise.success(function(data, status headers, config) {
			dummyUsers.push(this.user);
			this.user = {};
		});

		responsePromise.error(function(data, status headers, config) {
			//add error handling function
		});
	};

	this.login = function(){
		//Modeled off of http://tutorials.jenkov.com/angularjs/ajax.html
		$scope.myData = JSON.stringify({user: this.user.username, password: this.user.password});
		
		var responsePromise = $http.post(dummyURL.herokuapp.com/UserModel/login, $scope.myData);

		responsePromise.success(function(data, status headers, config) {
			//add success result
		});

		responsePromise.error(function(data, status headers, config) {
			//add error handling function
		});
	};

	this.logout = function(){
		this.user = {};
		
		$scope.myData = JSON.stringify({user: this.user.username, password: this.user.password}); //SEND COOKIES AS WELL
		
		var responsePromise = $http.post(dummyURL.herokuapp.com/UserModel/login, $scope.myData);

		responsePromise.success(function(data, status headers, config) {
			//add success result
		});

		responsePromise.error(function(data, status headers, config) {
			//add error handling function
		});

		//Add navigation for HTML
		//Save cookies to the backend
	}


});

app.controller('CardController', function($scope, $http){

	this.add_tag = function(tagName){

	};

	this.modify_tag = function(currentTagName, newTagName){

	};

	this.get_tags = function(tagName){

	};

	this.remove_tag = function(tagName){

	};

	this.create_card = function(companyName, jobTitle, status){
		
	};

	this.modify_card_status = function(cardId, updatedStatus){
		this.status = 
	};

	this.get_user_cards = function(tagName){

	};

});

app.controller('DocumentController', function($scope, $http) {
	
	this.upload_document = function(PDFdoc){

	};

	this.remove_document = function(docId){

	};

	this.get_documents = function(userId){

	};

});

var dummyUsers = [{
	username: 'seth',
	password: 'hello',
	email: 'sethanderson@berkeley.edu',
	id: 1234
}, {
	username: 'yaxin',
	password: 'goodbye',
	email: 'yaxin.t@berkeley.edu',
	id: 5678
}];

var dummyCards = [{
	companyName: 'Uber',
	jobTitle: 'Software Engineer',
	status: 0,
	tags: [
	'backend',
	'SF',
	'python'
	]
	id: 9999
}, {
	companyName: 'Uber',
	jobTitle: 'Sales Assistant',
	status: 1,
	tags: [
	'client-side',
	'SF',
	'low salary'
	]
	id: 5555
}, {
	companyName: 'Google',
	jobTitle: 'Software Engineer',
	status: 1,
	tags: [
	'frontend',
	'Mountain View',
	'good culture'
	]
	id: 3333
}];
