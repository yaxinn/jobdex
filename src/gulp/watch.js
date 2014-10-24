'use strict';

var gulp = require('gulp');

var $ = require('gulp-load-plugins')();

gulp.task('watch', ['styles'] ,function () {
  gulp.watch('static/styles/**/*.scss', ['styles']);
  gulp.watch('static/scripts/**/*.js', ['scripts']);
  gulp.watch('static/images/**/*', ['images']);
});
