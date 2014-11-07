app.controller('mainCtrl', function ($scope, $http, $cookies) {
    $scope.title = "Jobdex";
});

function error(xhr, ajaxOptions, thrownError) {
    console.log(xhr.responseText);
}

// Controller with all of the methods for the User Model
app.controller('UserController', function($scope, $http) {

    //This table is needed to store ids on the front end for some of the method calls to users
    //when using ng-repeat, set it to "user in userCtrl.cards", where userCtrl is the UserController alias
    var users = [{
        id: 9999
    }, {
        id: 5555
    }, {
        id: 3333
    }];

    // Send information on a new user to the backend and verify information
    $scope.sign_up = function(){

        var req = JSON.stringify({username: $scope.user.username, password: $scope.user.password, confirm_password: $scope.user.confirm_password, email: $scope.user.email});
        $http.post('/api/users', req).
    success(function(data, status, headers, config) {
        if (data.error_message <= 0) {
            $scope.errorHandler(data.error_message);
        }
        else if (data.error_message == 1){
            //Store the user id in the table above
            users.push(data.user_id_output);

            // direct user to the dashboard in html
        }
    }).error(function(data, status, headers, config) {
        //add error handling function
    });
$scope.user = {};
    };

    //Verify a user's login info
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

    //Once logout is selected, user should be brought back to the login page
    $scope.logout = function(){

        $http.get('/api/users').
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
    };

    //Return a List of all of the cards for a user
    $scope.get_user_cards = function(user){

        $http.get('/api/users/' + user.id + '/cards').
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

    //Return a List of all of the cards from a certain company, when given the company name
    $scope.get_company_cards = function(user){

        $http.get('/api/users/' + user.id + '/' + company_name + '/cards').
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
    };


});

//All methods dealing with cards are in this controller
app.controller('CardController', function($scope, $http){

    $http.get('/api/card/all-cards').
    success(function(data, status, headers, config) {
        console.log("SUCCESS");
        console.log(data);
        $scope.cards = data;
    }).
    error(function(data, status, headers, config) {
        console.log("ERROR");
        console.log(data);
    });

    //This table is needed to store ids on the front end for some of the method calls to cards
    //when using ng-repeat, set it to "id_entry in cardCtrl.id_table", where cardCtrl is the CardController alias
    var id_table = [];

    //add a tag to the tag given
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

    //Create a new card with a company name, job title, and initial status. 
    //The card's id should be returned and stored in the database.
    $scope.displayedCard = {};
    $scope.detailIsShown = false;
    $scope.showDetails = function(card) {
        //console.log($(angular.element(card)[0]).data('company'));
        $scope.displayedCard.company = $(angular.element(card)[0]).data('company');
        $scope.displayedCard.position = $(angular.element(card)[0]).data('position');
        $scope.displayedCard.notes = $(angular.element(card)[0]).data('notes');
        //$scope.displayedCard.contactName = $(angular.element(card)[0]).data('contactName');
        //$scope.displayedCard.contactEmail = $(angular.element(card)[0]).data('contactEmail');
        //$scope.displayedCard.contactPhone = $(angular.element(card)[0]).data('contactPhone');
        $scope.displayedCard.status = $(angular.element(card)[0]).data('status');
        $scope.detailIsShown = true;
    }
    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    $scope.create_card = function(){
        var req = JSON.stringify({companyName: $scope.card.companyName, 
            jobTitle: $scope.card.position,
            tags: $scope.card.tags,
            notes: $scope.card.notes,
            contactName: $scope.card.contactName,
            contactEmail: $scope.card.contactEmail,
            contactPhone: $scope.card.contactPhone,
            status: $scope.card.status});
        $http.post('/api/user/create-card', req).
            success(function(data, status, headers, config){
                console.log(data);

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_code);
                }
                else if (data.error_message == 1){
                    id_table.push(data.card_id);
                }

                location.reload();

            }).error(function(data, status, headers, config){
                console.log(data);
            });
        $scope.card = {};
    };

    //Change the status of a card (In Progress, Complete, Failed, or Interested)
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
    };

});

app.controller('DocumentController', function($scope, $http) {

    //Upload a PDF doc to the backend database for storage
    $scope.upload_document = function(){
        var req = JSON.stringify({name: $scope.doc.name, pdf: $scope.doc.PDFdoc});
        $http.post('/api/user/upload_document/', req).
    success(function(data, status, headers, config) {
        if (data.error_message <= 0) {
            $scope.errorHandler(data.error_message);
        }
        else if (data.error_message == 1){
            // success
        }
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
    };	

});


