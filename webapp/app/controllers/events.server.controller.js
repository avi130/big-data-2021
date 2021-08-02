var Predictions = require('mongoose').model('Predictions');
exports.create = function(req, res, next) {
    Predictions.find({status:'latest'}, function (err, docs) {
        console.log(docs)        
        if(docs){
            res.render('index', {
                title : 'CONFUSION MATRIX',

                p_1_1 : docs[0]['section_1']['predicted_1'],
                p_1_2 : docs[0]['section_1']['predicted_2'],
                p_1_3 : docs[0]['section_1']['predicted_3'],
                p_1_4 : docs[0]['section_1']['predicted_4'],
                p_1_5 : docs[0]['section_1']['predicted_5'],

                p_2_1 : docs[0]['section_2']['predicted_1'],
                p_2_2 : docs[0]['section_2']['predicted_2'],
                p_2_3 : docs[0]['section_2']['predicted_3'],
                p_2_4 : docs[0]['section_2']['predicted_4'],
                p_2_5 : docs[0]['section_2']['predicted_5'],

                p_3_1 : docs[0]['section_3']['predicted_1'],
                p_3_2 : docs[0]['section_3']['predicted_2'],
                p_3_3 : docs[0]['section_3']['predicted_3'],
                p_3_4 : docs[0]['section_3']['predicted_4'],
                p_3_5 : docs[0]['section_3']['predicted_5'],

                p_4_1 : docs[0]['section_4']['predicted_1'],
                p_4_2 : docs[0]['section_4']['predicted_2'],
                p_4_3 : docs[0]['section_4']['predicted_3'],
                p_4_4 : docs[0]['section_4']['predicted_4'],
                p_4_5 : docs[0]['section_4']['predicted_5'],

                p_5_1 : docs[0]['section_5']['predicted_1'],
                p_5_2 : docs[0]['section_5']['predicted_2'],
                p_5_3 : docs[0]['section_5']['predicted_3'],
                p_5_4 : docs[0]['section_5']['predicted_4'],
                p_5_5 : docs[0]['section_5']['predicted_5']

           })
       }
       else{
        console.log('check here')
        res.send('Refresing predictions, Please try after some time')
    }
})
};