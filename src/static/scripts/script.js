'use strict';

var app = angular.module('jobdex_app', ['ngCookies']);

$("#login").leanModal({top : 100, overlay : 0.6, closeButton: ".modal_close" });

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
