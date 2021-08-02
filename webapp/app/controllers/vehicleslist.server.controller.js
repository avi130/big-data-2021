const redis = require("redis");
const client = redis.createClient();

client.on("error", function(error) {
  console.error(error);
});
exports.listsection1 = function(req, res, next) {
  client.smembers('list_section_1',function(err,reply){
    console.log(reply)
    res.render('l1',{
      l1 : reply
    })
  })
};
exports.listsection2 = function(req, res, next) {
  client.smembers('list_section_2',function(err,reply){
    console.log(reply)
    res.render('l2',{
      l2 : reply
    })
  })
};
exports.listsection3 = function(req, res, next) {
  client.smembers('list_section_3',function(err,reply){
    console.log(reply)
    res.render('l3',{
      l3 : reply
    })
  })
};
exports.listsection4 = function(req, res, next) {
  client.smembers('list_section_4',function(err,reply){
    console.log(reply)
    res.render('l4',{
      l4 : reply
    })
  })
};
exports.listsection5 = function(req, res, next) {
  client.smembers('list_section_5',function(err,reply){
    console.log(reply)
    res.render('l5',{
      l5 : reply
    })
  })
};