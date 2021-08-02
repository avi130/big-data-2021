var express = require('./config/express');
var mongoose = require('./config/mongoose');
var db = mongoose();
var app = express();
app.listen(3000);
module.exports = app;
console.log('Server running at http://localhost:3000/');
