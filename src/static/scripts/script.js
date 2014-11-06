'use strict';

var app = angular.module('jobdex_app', ['ngCookies']);

$("#login").leanModal({top : 100, overlay : 0.6, closeButton: ".modal_close" });
$("#card_view").leanModal({top : 100, overlay : 0.6, closeButton: ".modal_close" });

// Calling Register Form
$(".create_account").click(function(){
    $(".user_register").show();
    $(".user_login").hide();
    $(".header_title").text('Register');
    return false;
});

$("#login").click(function() {
    $(".user_login").show();
    $(".user_register").hide();
    $(".header_title").text('Login');
    return false;
})

$("#card_view").click(function(){
    $("#card-detail-tabs").show()
    return false;
})

$("#main").click(function(){
    $("#main").show()
    $("#contacts").hide()
    $("#notes").hide()
    $("#tasks").hide()
    return false;
})

$("#contacts").click(function(){
    $("#contacts").show()
    $("#main").hide()
    $("#notes").hide()
    $("#tasks").hide()
    return false;
}) 

$("#notes").click(function(){
    $("#notes").show()
    $("#contacts").hide()
    $("#main").hide()
    $("#tasks").hide()
    return false;
}) 

$("#tasks").click(function(){
    $("#main").show()
    $("#contacts").hide()
    $("#notes").hide()
    $("#main").hide()
    return false;
})  
