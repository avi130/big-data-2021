var vehicleslist = require('../controllers/vehicleslist.server.controller');
module.exports = function(app) {
    app.route('/section1vehicles').get(vehicleslist.listsection1);
    app.route('/section2vehicles').get(vehicleslist.listsection2);
    app.route('/section3vehicles').get(vehicleslist.listsection3);
    app.route('/section4vehicles').get(vehicleslist.listsection4);
    app.route('/section5vehicles').get(vehicleslist.listsection5);
};