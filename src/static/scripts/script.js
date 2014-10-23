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

	$scope.modify_card_status = function(cardId, updatedStatus){

		$scope.myData = JSON.stringify({card_id: cardId, status: updatedStatus});
		var responsePromise = $http.post(dummyURL.herokuapp.com/CardModel/modify_card_status, $scope.myData);
		
		responsePromise.success(function(data, status, headers, config) {
			//add success result
		});

		responsePromise.error(function(data, status headers, config) {
			//add error handling function
		});		

	};

	$scope.get_user_cards = function(user){
		$scope.myData = JSON.stringify({username: user});
		var responsePromise = $http.get(dummyURL.herokuapp.com/CardModel/get_user_cards. $scope.myData);

		responsePromise.success(function(data, status, headers, config) {

		});

		responsePromise.error(function(data, status, headers, config){


		});
	};

});

app.controller('DocumentController', function($scope, $http) {
	
	$scope.upload_document = function(user, PDFdoc){
		$scope.myData = JSON.stringify({username: user, PDF: PDFdoc});
		var responsePromise = $http.post(dummyURL.herokuapp.com/DocumentModel/upload_document. $scope.myData);

		responsePromise.success(function(data, status, headers, config) {

		});

		responsePromise.error(function(data, status, headers, config){


		});
	};

	this.remove_document = function(doc_id){
		$scope.myData = JSON.stringify({username: user, docId: doc_id});
		var responsePromise = $http.post(dummyURL.herokuapp.com/DocumentModel/remove_document. $scope.myData);

		responsePromise.success(function(data, status, headers, config) {

		});

		responsePromise.error(function(data, status, headers, config){


		});
	};

	this.get_documents = function(user_id){
		$scope.myData = JSON.stringify({userId: user_id});
		var responsePromise = $http.get(dummyURL.herokuapp.com/DocumentModel/remove_document. $scope.myData);

		responsePromise.success(function(data, status, headers, config) {

		});

		responsePromise.error(function(data, status, headers, config){


		});
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
