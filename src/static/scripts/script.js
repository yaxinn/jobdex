'use strict';

var app = angular.module('jobdex_app', ['ngCookies']);

app.controller('UserController', function() {
	this.user = {};

	this.sign_up = function(){		
		// if user is valid
		dummyUsers.push(this.user);
		this.user = {};
	};

	this.login = function(){
		$
	};


});

app.controller('TagController', function(cardId) {
	
	this.cardId = cardId;

	this.addTag = function(tagName){

	};

	this.modifyTag = function(currentTagName, newTagName){

	};

	this.getTags = function(tagName){

	};

	this.removeTag = function(tagName){

	};

});

app.controller('CardController', function(status){

	this.status = status

	this.createCard = function(companyName, jobTitle, status){
		
	};

	this.modifyCardStatus = function(cardId, updatedStatus){
		this.status = 
	};

	this.getUserCards = function(tagName){

	};

});

app.controller('DocumentController', function() {
	
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
