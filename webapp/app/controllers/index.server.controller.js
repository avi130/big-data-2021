const redis = require("redis");
const client = redis.createClient();

client.on("error", function(error) {
  console.error(error);
});

exports.render = function(req, res) {
  client.get('sections_vehicles_nos',function(err,reply){
    console.log(reply)
    const reply_1 = JSON.parse(reply)
    res.render('home', {
      title: 'Big Data Project',
      s_1: reply_1["v1"],
      s_2: reply_1["v2"],
      s_3: reply_1["v3"],
      s_4: reply_1["v4"],
      s_5: reply_1["v5"]

  })
  })
};
