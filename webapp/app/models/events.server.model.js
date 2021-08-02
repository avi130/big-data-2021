var mongoose = require('mongoose'),
Schema = mongoose.Schema;
var PredictionsSchema = new Schema({
    status:String,
    section_1:{
        predicted_1:Number,
        predicted_2:Number,
        predicted_3:Number,
        predicted_4:Number,
        predicted_5:Number
    },
    section_2:{
        predicted_1:Number,
        predicted_2:Number,
        predicted_3:Number,
        predicted_4:Number,
        predicted_5:Number
    },
    section_3:{
        predicted_1:Number,
        predicted_2:Number,
        predicted_3:Number,
        predicted_4:Number,
        predicted_5:Number
    },
    section_4:{
        predicted_1:Number,
        predicted_2:Number,
        predicted_3:Number,
        predicted_4:Number,
        predicted_5:Number
    },
    section_5:{
        predicted_1:Number,
        predicted_2:Number,
        predicted_3:Number,
        predicted_4:Number,
        predicted_5:Number
    }
}
);
mongoose.model('Predictions', PredictionsSchema);