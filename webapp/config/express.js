var express = require('express');
module.exports = function() {
var app = express();
app.set('views', './app/views');
app.set('view engine', 'ejs');
require('../app/routes/index.server.routes.js')(app);
require('../app/routes/vehicles.server.routes.js')(app);
require('../app/routes/vehicleslist.server.routes.js')(app);
require('../app/routes/events.server.routes.js')(app);
return app;
};
