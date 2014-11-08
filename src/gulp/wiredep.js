'use strict';

var gulp = require('gulp');

var $ = require('gulp-load-plugins')();

// inject bower components
gulp.task('wiredep', function () {
  var wiredep = require('wiredep').stream;

  gulp.src('static/styles/*.scss')
    .pipe(wiredep({
        directory: 'static/bower_components'
    }))
    .pipe(gulp.dest('static/styles'));

});
