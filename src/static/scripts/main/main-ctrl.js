app.controller('mainCtrl', function ($scope, $http, $cookies) {
    $scope.title = "Jobdex";
});

function error(xhr, ajaxOptions, thrownError) {
    console.log(xhr.responseText);
}

// error code
var SUCCESS = 1;
var ERR_TAG_EXISTS = -1;
var ERR_TAG_INVALID = -2;
var ERR_TAG_DOES_NOT_EXIST = -3;
var ERR_COMPANY_EXISTS = -4;
var ERR_COMPANY_INVALID = -5;
var ERR_COMPANY_DOES_NOT_EXIST = -6;
var ERR_CARD_EXISTS = -7;
var ERR_CARD_DOES_NOT_EXIST = -8;
var ERR_DOC_EXISTS = -9;
var ERR_DOC_INVALID = -10;
var ERR_DOC_DOES_NOT_EXIST = -11;
var ERR_CONTACT_EXISTS = -12;
var ERR_CONTACT_INVALID = -13;
var ERR_CONTACT_DOES_NOT_EXIST = -14;
var ERR_TAST_EXISTS = -15;
var ERR_TASK_INVALID = -16;
var ERR_TASK_DOES_NOT_EXIST = -17;

var ERR_BAD_CREDENTIALS = -18;
var ERR_EXISTING_USER = -19;
var ERR_BAD_USERNAME = -20;
var ERR_BAD_PASSWORD = -21;

var ERR_NOTE_INVALID = -22;


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

    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    // Dont know what this part is.
    //     $http.get('/api/card/all-cards').
    //         success(function(data, status, headers, config) {
    //             console.log("SUCCESS");
    //             console.log(data);
    //             $scope.cards = data;
    //         }).error(function(data, status, headers, config) {
    //             console.log("ERROR");
    //             console.log(data);
    //     });

    //This table is needed to store ids on the front end for some of the method calls to cards
    //when using ng-repeat, set it to "id_entry in cardCtrl.id_table", where cardCtrl is the CardController alias
    var id_table = [];

// Card
    //Create a new card with a company name, job title, and initial status. 
    //The card's id should be returned and stored in the database.
    $scope.displayedCard = {};
    $scope.displayedCard.contactList = [];
    $scope.detailIsShown = false;
    $scope.isEditing = false;
    $scope.isStatusEditing = false;
    $scope.isContactEditing = false;
    $scope.isContactAdding = false;
    $scope.isNotesEditing= false;
    $scope.isTagAdding= false;
    $scope.isTagRemoving= false;
    $scope.edit = function() {
       if ($scope.isEditing){
            $scope.isEditing = false;
        }
        else{
           $scope.isEditing = true; 
        } 
    }
    $scope.editStatus = function() {
       if ($scope.isStatusEditing){
            $scope.isStatusEditing = false;
        }
        else{
           $scope.isStatusEditing = true; 
        } 
    }
    $scope.editContact = function() {
       if ($scope.isContactEditing){
            $scope.isContactEditing = false;
        }
        else{
           $scope.isContactEditing = true; 
        } 
    }
    $scope.editAddContact = function() {
       if ($scope.isContactAdding){
            $scope.isContactAdding = false;
        }
        else{
           $scope.isContactAdding = true; 
        } 
    }
    $scope.editNotes = function() {
       if ($scope.isNotesEditing){
            $scope.isNotesEditing= false;
        }
        else{
           $scope.isNotesEditing = true; 
        } 
    }
    $scope.editAddTags = function() {
       if ($scope.isTagAdding){
            $scope.isTagAdding= false;
        }
        else{
           $scope.isTagAdding = true; 
        } 
    }
    $scope.editRemoveTags = function() {
       if ($scope.isTagRemoving){
            $scope.isTagRemoving= false;
        }
        else{
           $scope.isTagRemoving = true; 
        } 
    }
    $scope.closeEdit = function() {
       $scope.isEditing = false;
       $scope.isContactEditing = false;
       $scope.isNotesEditing= false;
       $scope.isTagAdding= false;
       $scope.isTagRemoving= false;
       $scope.isStatusEditing = false; 
    }
    $scope.closeDetails = function() {
        $scope.detailIsShown = false;
    }
    $scope.showDetails = function(card) {
        //console.log($(angular.element(card)[0]).data('company'));
        $scope.displayedCard.company = $(angular.element(card)[0]).data('company');
        $scope.displayedCard.position = $(angular.element(card)[0]).data('position');
        $scope.displayedCard.notes = $(angular.element(card)[0]).data('notes');
        $scope.displayedCard.tags = $(angular.element(card)[0]).data('tags').split(",");
        $scope.displayedCard.contacts = $(angular.element(card)[0]).data('contacts').split(",");
        $scope.displayedCard.contactName = $scope.displayedCard.contacts[0];
        $scope.displayedCard.contactEmail = $scope.displayedCard.contacts[1];
        $scope.displayedCard.contactPhone = $scope.displayedCard.contacts[2];
        $scope.displayedCard.status = $(angular.element(card)[0]).data('status');
        $scope.displayedCard.id = $(angular.element(card)[0]).data('id');
        $scope.detailIsShown = true;
        var contactObj = {};
        for (var i = 0; i < $scope.displayedCard.contacts.length; i+=3){
            
            contactObj.name = $scope.displayedCard.contacts[i];
            console.log(contactObj.name);
            contactObj.email = $scope.displayedCard.contacts[i+1];
            console.log(contactObj.email);
            contactObj.phone = $scope.displayedCard.contacts[i+2];
            console.log(contactObj.phone);

            $scope.displayedCard.contactList.push(contactObj);
            contactObj = {};
        }

        
    }

    $scope.create_card = function(){

        var req = JSON.stringify({companyName: $scope.card.companyName, 
            jobTitle: $scope.card.position,
            tags: $scope.card.tags,
            notes: $scope.card.notes,
            contactName: $scope.card.contactName,
            contactEmail: $scope.card.contactEmail,
            contactPhone: $scope.card.contactPhone,
            status: $scope.card.status});

        $http.post('/api/user/create-card/', req).
            success(function(data, status, headers, config){
                console.log(data);

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
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

    //remove card given user and card_id
    $scope.remove_card = function(card){
        var cardID = $(angular.element(card)[0]).data('unique_id');
        var req = {card_id: cardID};

        $http.post('/api/user/remove-card/', req).
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    error(data)
                }
                else if (data.error_message == 1) {
                    location.reload(true);
                }
            }).error(function(data, status, headers, config){
                console.log(data);
        });
    };

    //Change the status of a card (In Progress, Complete, Failed, or Interested)
    $scope.changeStatus = function(){
        var cardId = $scope.displayedCard.id;
        var newStatus = $scope.newStatus;

        var req = {card_id: cardId, new_status: newStatus};

        $http.post('/api/card/modify-card-status/', req).
            success(function(data, status, headers, config) {

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    // change the card status in the html
                    location.reload(true);
                }

            }).error(function(data, status, headers, config) {
                console.log(data); 
        });     
    };


// Tag
    //add a tag to the tag given
    $scope.add_tag = function(){
        var card_id = $scope.displayedCard.id;
        var tags = $scope.new_tags

        var req = JSON.stringify({card_id: card_id, tags: tags});
        
        $http.post('/api/user/add-tag/', req).
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    location.reload();
                }
            }).error(function(data, status, headers, config){
            //Handle error
        });
    };

    /*$scope.changeTag = function(){
        var cardId = $scope.displayedCard.id;
        var newTag = $scope.newTag;

        var req = {card_id: cardID, new_tag: newTag};
        
        $http.post('/api/card/modify-tag', req).
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    $scope.tags.splice($scope.currentTagIndex, 1);
                    $scope.tags.push(newTag);
                    location.reload(true);
                }

            }).error(function(data, status, headers, config){
                //Handle error
                console.log(data);
        });

    };*/

    $scope.get_tags = function(cardID){

        $http.get('/api/card/' + card_ID + '/tags').
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    $scope.tags = data.tags;
                    // in html, inside the CardController, use 'tags' to refer to the return tags
                    location.reload();
                }
            }).error(function(data, status, headers, config){
             //Handle error
        });

    };

    // remove the tag given cardID and tagName
    $scope.remove_tag = function(){
        //$scope.tagIndex = $scope.tags.indexOf(tagName);
        var card_id = $scope.displayedCard.id;
        var old_tag = $scope.old_tag;

        var req = JSON.stringify({card_id: card_id, old_tag: old_tag});
        
        $http.post('/api/user/remove-tag/', req).
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    location.reload();
                }
            }).error(function(data, status, headers, config){
            //Handle error
        });
    };



//contact
    //add contact for the given card_id
    $scope.add_contact = function(cardID){

        var card_id = $scope.displayedCard.id;
        var add_name = $scope.add_name;
        var add_email = $scope.add_email;
        var add_phone = $scope.add_phone;

        var req = JSON.stringify(
            {card_id: card_id, 
            add_name: add_name, 
            add_email: add_email,
            add_phone: add_phone,
        });

        $http.post('/api/card/add-contact/', req).
            success(function(data, status, headers, config){

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    location.reload();
                }


            }).error(function(data, status, headers, config){
                console.log(data);
        });
    };

    //Add task for a given card_id
    $scope.add_task = function(cardID){

        var card_id = $scope.displayedCard.id;
        var new_task = $scope.new_task;

        var req = JSON.stringify({card_id: card_id, 
            new_task: new_task});

        $http.post('/api/card/add-task/', req).
            success(function(data, status, headers, config){

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    location.reload();
                }


            }).error(function(data, status, headers, config){
                console.log(data);
        });
    };

    // Edit notes.
    $scope.edit_notes = function() {
        var card_id = $scope.displayedCard.id;
        var new_notes = $scope.new_notes;
        var req = {card_id: card_id, new_notes: new_notes}

        $http.post('/api/card/edit-notes/', req).
            success(function(data, status, headers, config) {

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    // change the card status in the html
                    location.reload(true);
                }

            }).error(function(data, status, headers, config) {
                console.log(data); 
        });  
    }

    //Change the status of a card (In Progress, Complete, Failed, or Interested)
    $scope.edit_contact = function(oldName) {
        var card_id = $scope.displayedCard.id;
        var new_name = $scope.new_name;
        var new_email = $scope.new_email;
        var new_phone = $scope.new_phone;
        var current_name = oldName;

        var req = {card_id: card_id, new_name: new_name, new_email: new_email, new_phone: new_phone, current_name: oldName};
        $http.post('/api/card/edit-contact/', req).
            success(function(data, status, headers, config) {

                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    // change the card status in the html
                    location.reload(true);
                }

            }).error(function(data, status, headers, config) {
                console.log(data); 
        });     
    };

    //remove a contact given card_id and contact.name
    $scope.remove_contact = function(cardID){

        var req = JSON.stringify({card_id: cardID, contactName: $scope.contact.name});

        $http.delete('/api/card/' + cardID + '/remove-contact', req).
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message)
                }
                else if (data.error_message == 1) {
                    location.reload(true);
                }
            }).error(function(data, status, headers, config){

        });
    };

    $scope.get_contacts = function(cardID){

        $http.get('/api/card/' + card_ID + '/contacts').
            success(function(data, status, headers, config){
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    $scope.contacts = data.contacts_output;
                    // in html, inside the CardController, use 'contacts' to refer to the return contacts
                }
            }).error(function(data, status, headers, config){
             //Handle error
        });

    };


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
        else if (error_message == ERR_COMPANY_EXISTS){
            console.log("The company you are trying to create already exists.");
        }
        else if (error_message == ERR_COMPANY_INVALID){
            console.log("Please make sure your Company name is valid and under 128 characters.");
        }
        else if (error_message == ERR_COMPANY_DOES_NOT_EXIST){
            console.log("The company does not exist.");
        }
        else if (error_message == ERR_CARD_EXISTS){
            console.log("The card already exist.");
        }
        else if (error_message == ERR_CARD_DOES_NOT_EXIST){
            console.log("The card does not exist.");
        }
        else if (error_message == ERR_CONTACT_EXISTS){
            console.log("The contact already exist.");
        }
        else if (error_message == ERR_CONTACT_INVALID){
            console.log("Please make sure the contact you create is valid.");
        }
        else if (error_message == ERR_CONTACT_DOES_NOT_EXIST){
            console.log("The contact does not exist.");
        }
        else if (error_message == ERR_TASK_EXISTS){
            console.log("The task already exist.");
        }
        else if(error_message == ERR_TASK_INVALID){
            console.log("Please make sure the task you create is valid.");
        }
        else if (error_message == ERR_TASK_DOES_NOT_EXIST) {
            console.log("The task does not exist.");
        }
    };

});


// app.service('pdf_upload', ['$http', function ($http) {

//     this.uploadPdf = function(file, uploadUrl){
//         var formdata = new FormData();
//         formdata.append('file', file);
        
//         $http.post(uploadUrl, formdata, {
//                 transformRequest: angular.identity,
//                 headers: {'Content-Type': undefined}
//             }).success(function(){

//             }).error(function(){
            
//             });
// }}]);

app.controller('DocumentController', function($scope, $http) {

    //Upload a PDF doc to the backend database for storage
    $scope.upload_document = function(){
        
        var req = JSON.stringify({name: $scope.doc.name, pdf: $scope.file});
        
        //pdf_upload.uploadPdf($scope.doc.PDFdoc, '/api/user/upload_document/')

        $http.post('/api/user/upload_document/', req).
            success(function(data, status, headers, config) {
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    location.reload(true);
                }
            }).error(function(data, status, headers, config){

        });

        $scope.doc = {};
    };

    // $scope.uploadFile = function(){
    //     var file = $scope.myFile;
    //     console.log('file is ' + JSON.stringify(file));
    //     var uploadUrl = "/fileUpload";
    //     fileUpload.uploadFileToUrl(file, uploadUrl);
    // };

    //remove a PDF document given the doc_id
    $scope.remove_document = function(){

        var req = JSON.stringify({doc_id: $scope.doc.id});
        
        $http.delete('/api/user/remove-document/', req).
            success(function(data, status, headers, config) {
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    location.reload();
                }
            }).error(function(data, status, headers, config){

        });
    };

    $scope.get_documents = function(userID){

        var req = JSON.stringify({user_id: userID});
        
        $http.get('/api/users/' + userID + '/documents', req).
            success(function(data, status, headers, config) {
                if (data.error_message <= 0) {
                    $scope.errorHandler(data.error_message);
                }
                else if (data.error_message == 1){
                    $scope.documents = data.documents_output;
                }
            }).error(function(data, status, headers, config){

         });
    };


    $scope.errorHandler = function(error_message) {

        if (error_message == ERR_DOC_EXISTS){
            console.log("Document already exist");
        }
        else if (error_message == ERR_DOC_INVALID){
            console.log("Please make sure the document is valid.");
        }
        else if (error_message == ERR_DOC_DOES_NOT_EXIST) {
            console.log("The document does not exist.");
        }
    };  
});


