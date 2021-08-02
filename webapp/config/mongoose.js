mongoose = require('mongoose');
module.exports = function() {
    var db = mongoose.connect("mongodb+srv://test:test@cluster0.vk3wu.mongodb.net/test?retryWrites=true&w=majority");
    require('../app/models/events.server.model');
    return db;
};