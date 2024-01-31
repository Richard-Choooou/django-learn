const { src, dest, watch } = require('gulp');
const sass = require('gulp-sass')(require('sass'))
const sourcemaps = require('gulp-sourcemaps');
const babel = require('gulp-babel')

const ts = (cb) => {
    src('*/static/**/*.ts', {base: './'})
        .pipe(sourcemaps.init())
        .pipe(
            babel({
                presets: ['@babel/env', '@babel/preset-typescript']
            })
        ).pipe(sourcemaps.write('.')).pipe(dest('./'))
    cb()
}

const scss = (cb) => {
    src('*/static/**/*.scss', {base: './'}).pipe(sass().on('error', sass.logError))
        .pipe(dest('./'))
    cb()
}

exports.dev = () => {
    watch("*/static/**/*.ts", ts)
    watch("*/static/**/*.scss", scss)
}


exports.jsEntry = (cb) => {

    cb();
}