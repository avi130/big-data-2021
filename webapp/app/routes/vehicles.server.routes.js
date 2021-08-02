var vehicles = require('../../app/controllers/vehicles.server.controller');
module.exports = function(app) {
    app.route('/section1').get(vehicles.section1);
    app.route('/section2').get(vehicles.section2);
    app.route('/section3').get(vehicles.section3);
    app.route('/section4').get(vehicles.section4);
    app.route('/section5').get(vehicles.section5);
};