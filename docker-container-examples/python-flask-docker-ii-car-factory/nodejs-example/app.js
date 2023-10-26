// very simple node.js express app to handle webhook calls for CarsFactory

// init project
var express = require('express');
var path = require('path');
var logger = require('morgan');
var index = require('./routes/index');
var app = express();


// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// set path for static assets
app.use(express.static(path.join(__dirname, 'public')));

//routes
app.use('/', index);


// catch 404 and forward to error handler
app.use(function(req, res, next) {
    res.status(404).send('Sorry cant find that!');
}

// error handler
app.use(function(err, req, res, next) {
    res.status(500).send('Something broke!');
}