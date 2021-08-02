var events = require('../../app/controllers/events.server.controller');
module.exports = function(app) {
app.route('/confusionmatrix').get(events.create);
};