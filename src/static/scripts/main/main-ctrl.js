app.controller('mainCtrl', function ($scope, $http, $cookies) {
    $scope.title = "Jobdex";
});

function error(xhr, ajaxOptions, thrownError) {
    console.log(xhr.responseText);
}

// 
app.controller('UserController', function($scope, $http) {

	// 
	$scope.sign_up = function(){
		
		var req = JSON.stringify({username: $scope.user.username, password: $scope.user.password, confirm_password: $scope.user.confirm_password, email: $scope.user.email});
		$http.post('/api/users', req).
			success(function(data, status, headers, config) {
				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					// direct user to the dashboard in html
				}
			}).error(function(data, status, headers, config) {
			//add error handling function
		});
		$scope.user = {};
	};

	$scope.login = function(){
		
		var req = JSON.stringify({username: $scope.user.username, password: $scope.user.password});
		$http.post('/api/users', req).
			success(function(data, status, headers, config) {
				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					// sucess
				}
			}).error(function(data, status, headers, config) {
			//add error handling function
		});
		$scope.user = {};
	};

	$scope.logout = function(){

		var req = JSON.stringify({});
		$http.get('/api/users', req).
			success(function(data, status, headers, config) {
			//add success result
				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					// sucess 
				}
			}).error(function(data, status, headers, config) {
			//add error handling function
		});
		$scope.user = {};
		//Add navigation for HTML
		//Save cookies to the backend
	}

	var ERR_BAD_CREDENTIALS = -1;
	var ERR_EXISTING_USER = -2;
	var ERR_BAD_USERNAME = -3;
	var ERR_BAD_PASSWORD = -4;

	$scope.errorHandler = function(error_message) {
		if (error_message == ERR_BAD_CREDENTIALS){
			console.log("Bad Credential");
		}
		else if (error_message == ERR_EXISTING_USER){
			console.log("User Exists");
		}
		else if (error_message == ERR_BAD_USERNAME){
			console.log("Bad Username");
		} 
		else if (error_message == ERR_BAD_PASSWORD){
			console.log("BAD_PASSWORD");
		}
	}


});

app.controller('CardController', function($scope, $http){
	//when using ng-repeat, set it to "id_entry in cardCtrl.id_table", where cardCtrl is the CardController alias
	var id_table = [{
		id: 9999
	}, {
		id: 5555
	}, {
		id: 3333
	}];


	$scope.add_tag = function(id_entry){

		var req = JSON.stringify({card_id: id_entry.id, tags: $scope.card.tags});
		$http.post('/api/card/' + id_entry.id + '/add-tag', req).success(function(data, status, headers, config){

		if (data.error_message <= 0) {
			$scope.errorHandler(data.error_message);
		}
		else if (data.error_message == 1){
			$scope.tags.push(tagName);
		}
		}).error(function(data, status, headers, config){
				//Handle error
		});
		$scope.card = {};
	};

	// this is for next iteration
	// $scope.modify_tag = function(currentTagName, newTagName){

	// 	$scope.currentTagIndex = $scope.tags.indexOf(currentTagName);

	// 	var req = JSON.stringify( {currentTagName: 'currentTagName', newTagName: newTagName});
	// 	$http.post('/modify-tag.json', req).
	// 		success(function(data, status, headers, config){
				
	// 			if (data.error_message <= 0) {
	// 				$scope.errorHandler(data.error_message);
	// 			}
	// 			else if (data.error_message == 1){
	// 				$scope.tags.splice($scope.currentTagIndex, 1);
	// 			$scope.tags.push(tagName);
	// 			}

	// 	}).error(function(data, status, headers, config){
	// 		//Handle error
	// 	});

	// };

	// $scope.get_tags = function(tagName){

	// 	$http.get('/get-tags.json').
	// 		success(function(data, status, headers, config){
	// 			if (data.error_message <= 0) {
	// 					$scope.errorHandler(data.error_message);
	// 				}
	// 				else if (data.error_message == 1){
	// 					return data.tags;
	// 				}
	// 		}).error(function(data, status, headers, config){
	// 			//Handle error
	// 	});

	// };

	// $scope.remove_tag = function(cardId, tagName){

	// 	$scope.tagIndex = $scope.tags.indexOf(tagName);

	// 	$http.post('/modify-tag.json', {currentTagName: currentTagName, newTagName: newTagName}).
	// 		success(function(data, status, headers, config){
				
	// 			if (data.error_message <= 0) {
	// 				$scope.errorHandler(data.error_message);
	// 			}
	// 			else if (data.error_message == 1){
	// 				$scope.tags.splice($scope.tagIndex, 1);
	// 			}

	// 		}).error(function(data, status, headers, config){
	// 		//Handle error
	// 	});
	// };

	$scope.create_card = function(){
	
		var req = JSON.stringify({company_name: $scope.card.company_name, job_title: $scope.card.job_title, status: $scope.card.status});
		$http.post('/api/user/create-card', req).
			success(function(data, status, headers, config){
				
				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					//add the new card_id to the cards table
					cards.push(data.card_id_output);
				}

			}).error(function(data, status, headers, config){
			//Handle error
		});
		$scope.card = {};

	};

	$scope.modify_card_status = function(id_entry){
		var req = JSON.stringify({card_id: id_entry.id, status: $scope.card.status});
		$http.post('/api/card/' + id_entry.id + '/status', req).
			success(function(data, status, headers, config) {
				
				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					// change the card status in the html
				}

			}).error(function(data, status, headers, config) {
			//add error handling function
		});		

	};


	$scope.get_company_cards = function(){

		var req = JSON.stringify({company_name: $scope.card.company_name});

		$http.get('/', req).
			success(function(data, status, headers, config) {

				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					// in the html, use cardList to display company cards
					$scope.cardList = data.cards_output;
				}

			}).error(function(data, status, headers, config){

		});
	};

	var ERR_TAG_EXISTS = -1;
	var ERR_TAG_INVALID = -2;
	var ERR_TAG_DOES_NOT_EXIST = -3;
	var ERR_INVALID_COMPANY = -4;
	var ERR_INVALID_JOB = -5;
	var ERR_NO_CARDS = -6;

	$scope.errorHandler = function(error_message) {
		if (error_message == ERR_TAG_EXISTS){
			console.log("$scope card already contains $scope tag.");
		}
		else if (error_message == ERR_TAG_INVALID){
			console.log("Please make sure your tag is less than 128 characters.");
		}
		else if (error_message == ERR_TAG_DOES_NOT_EXIST){
			console.log("The tag you are searching for does not extist.");
		} 
		else if (error_message == ERR_INVALID_COMPANY){
			console.log("Please make sure your Company name is valid and under 128 characters.");
		}
		else if (error_message == ERR_INVALID_JOB){
			console.log("Please make sure your Job title is valid and under 128 characters.");
		}
		else if (error_message == ERR_NO_CARDS){
			console.log("There are currently no cards for $scope user.");
		}
	}

}]);

app.controller('DocumentController', function($scope, $http) {
	
	$scope.upload_document = function(){
		var req = JSON.stringify({name: $scope.doc.name, pdf: $scope.doc.PDFdoc});
		$http.post('/api/user/upload_document/', req).
			success(function(data, status, headers, config) {
				if (data.error_message <= 0) {
					$scope.errorHandler(data.error_message);
				}
				else if (data.error_message == 1){
					// sucess
			}).error(function(data, status, headers, config){

		});
		$scope.doc = {};
	};

	// this is for next iteration
	// $scope.remove_document = function(doc_id){
	// 	var req = JSON.stringify({name: $scope.doc.name});
	// 	$http.post('/remove_document.json', req).
	// 		success(function(data, status, headers, config) {
	// 			if (data.error_message <= 0) {
	// 				$scope.errorHandler(data.error_message);
	// 			}
	// 			else if (data.error_message == 1){
	// 				// sucess
	// 			}
	// 		}).responsePromise.error(function(data, status, headers, config){


	// 	});
	// };

	// $scope.get_documents = function(user_id){

	// 	var req = JSON.stringify()
	// 	$http.get('/get_documents.json', {userId: user_id}).
	// 		success(function(data, status, headers, config) {
	// 			if (data.error_message <= 0) {
	// 				$scope.errorHandler(data.error_message);
	// 			}
	// 			else if (data.error_message == 1){
	// 				// sucess
	// 			}
	// 		}).responsePromise.error(function(data, status, headers, config){


	// 	});
	// };

	var ERR_DOC_NOTFOUND = -1;
	var ERR_DOC_EXISTS = -2;

	$scope.errorHandler = function(error_message) {
		if (error_message == ERR_DOC_NOTFOUND){
			console.log("Document Not Found");
		}
		else if (error_message == ERR_DOC_EXISTS){
			console.log("Document Exists");
		}
	}	

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



var dummyDocuments = [{
	docName: 'resume_softwareEngineer',
	type: 'pdf',
	url: '',
}, {
	docName: 'resume_salesAssistant',
	type: 'pdf',
	url: '',
}]

