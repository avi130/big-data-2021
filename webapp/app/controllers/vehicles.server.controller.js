const redis = require("redis");
const client = redis.createClient();

client.on("error", function(error) {
  console.error(error);
});
exports.section1 = function(req, res, next) {
  client.get('section_1',function(err,reply){
    res.send('No of vehicles in section 1 : '+reply)
  })
};
exports.section2 = function(req, res, next) {
  client.get('section_2',function(err,reply){
    res.send('No of vehicles in section 2 : '+reply)
  })
};
exports.section3 = function(req, res, next) {
  client.get('section_3',function(err,reply){
    res.send('No of vehicles in section 3 : '+reply)
  })
};
exports.section4 = function(req, res, next) {
  client.get('section_4',function(err,reply){
    res.send('No of vehicles in section 4 : '+reply)
  })
};
exports.section5 = function(req, res, next) {
  client.get('section_5',function(err,reply){
    res.send('No of vehicles in section 5 : '+reply)
  })
};