'use strict';

var app = angular.module('jobdex_app', ['ngCookies']);

$("#login").leanModal({top : 100, overlay : 0.6, closeButton: ".modal_close" });

//var documentURL = document.getElementById('document-url').getAttribute("href");
//console.log(documentURL);
PDFJS.workerSrc = "/static/bower_components/pdf.worker.js";
//PDFJS.getDocument(documentURL).then(function(pdf) {
//  // Using promise to fetch the page
//  pdf.getPage(1).then(function(page) {
//    var scale = 1.5;
//    var viewport = page.getViewport(scale);
//
//    //
//    // Prepare canvas using PDF page dimensions
//    //
//    var canvas = document.getElementById('the-canvas');
//    var context = canvas.getContext('2d');
//    canvas.height = viewport.height;
//    canvas.width = viewport.width;
//
//    //
//    // Render PDF page into canvas context
//    //
//    var renderContext = {
//      canvasContext: context,
//      viewport: viewport
//    };
//    page.render(renderContext);
//  });
//});

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
});


jQuery(document).ready(function() {

    jQuery('#tab-links a').on('click', function(e)  {

        var currentAttrValue = jQuery(this).attr('href');

        // Show/Hide Tabs
        jQuery('#card-detail-tabs ' + currentAttrValue).siblings().hide();
        jQuery('#card-detail-tabs ' + currentAttrValue).show();

        // Change/remove current tab to active
        jQuery(this).parent('li').addClass('active-tab').siblings().removeClass('active-tab');
        e.preventDefault();
    });

    $("#tab-links .active-tab a").click();

});

$(function() {
    $(document).tooltip();
  });