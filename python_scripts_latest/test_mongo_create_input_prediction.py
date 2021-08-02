#this script creates the input for prediction sent to BigML

from pymongo import MongoClient
from bigml.ensemble import Ensemble
from bigml.api import BigML
import time

import redis

#setting up redis connection

r = redis.Redis(
    host='127.0.0.1',
    port=6379)


#setting up ensemble connection

ensemble = Ensemble('ensemble/61085e0f5e269e0554018f9f',
                    api=BigML("bgidataproject2021",
                              "e8dd610fb20cacb4420d55a4d7d4630dc5e8024a",
                              domain="bigml.io"))

#setting up mongodb connection

client = MongoClient("mongodb+srv://test:test@cluster0.vk3wu.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
events = db.events_2
predictions = db.predictions
predictions_actual = db.predictions_actual

#create a continuous loop

while(1==1):
    predicted = {}

    predicted_dict_1 = {}
    predicted_dict_1['predicted_1'] = 0
    predicted_dict_1['predicted_2'] = 0
    predicted_dict_1['predicted_3'] = 0
    predicted_dict_1['predicted_4'] = 0
    predicted_dict_1['predicted_5'] = 0

    predicted_dict_2 = {}
    predicted_dict_2['predicted_1'] = 0
    predicted_dict_2['predicted_2'] = 0
    predicted_dict_2['predicted_3'] = 0
    predicted_dict_2['predicted_4'] = 0
    predicted_dict_2['predicted_5'] = 0

    predicted_dict_3 = {}
    predicted_dict_3['predicted_1'] = 0
    predicted_dict_3['predicted_2'] = 0
    predicted_dict_3['predicted_3'] = 0
    predicted_dict_3['predicted_4'] = 0
    predicted_dict_3['predicted_5'] = 0

    predicted_dict_4 = {}
    predicted_dict_4['predicted_1'] = 0
    predicted_dict_4['predicted_2'] = 0
    predicted_dict_4['predicted_3'] = 0
    predicted_dict_4['predicted_4'] = 0
    predicted_dict_4['predicted_5'] = 0

    predicted_dict_5 = {}
    predicted_dict_5['predicted_1'] = 0
    predicted_dict_5['predicted_2'] = 0
    predicted_dict_5['predicted_3'] = 0
    predicted_dict_5['predicted_4'] = 0
    predicted_dict_5['predicted_5'] = 0
    
    #get vehicles list from redis

    vehicles_total_1 = r.get('vehicles_total')
    vehicles_total = int(vehicles_total_1.decode("utf-8"))
    print(vehicles_total)

    #c = predictions.delete_many({})
    #print('predictions deleted : ' + str(c.deleted_count))

    #loop over the vehicles list

    for j in range(100001, vehicles_total):
        dict_1 = {}

        dict_1['vehicle_no'] = j

        dict_1['exiting_section'] = 0
        dict_1['entering_section'] = 0
        #get the vehicles data from mongodb   
        for docs in events.find({'vehicle_no': j}):
            if docs['event_type'] == 'entering_road':
                dict_1['entering_section'] = docs['section']
            if docs['event_type'] == 'exiting_road':
                dict_1['exiting_section'] = docs['section']
            dict_1['day'] = docs['day']
            dict_1['hour'] = docs['hour']
            dict_1['special_day'] = docs['special_day']
    
        dict_1['switching_sections_12'] = 0
        dict_1['switching_sections_23'] = 0
        dict_1['switching_sections_34'] = 0
        dict_1['switching_sections_45'] = 0
    
        dict_1['switching_sections_21'] = 0
        dict_1['switching_sections_32'] = 0
        dict_1['switching_sections_43'] = 0
        dict_1['switching_sections_54'] = 0
        #exit the loop of the vehicle has not done exit
        if dict_1['exiting_section'] == 0:
            continue
        #set the switching sections if entering section < exit section
        if (dict_1['entering_section'] < dict_1['exiting_section']) and dict_1['exiting_section'] != 0:
            for docs in events.find({'vehicle_no': j}):
                if docs['event_type'] == 'entering_section':
                    if docs['section'] == 2:
                        dict_1['switching_sections_12'] = 1
                    if docs['section'] == 3:
                        dict_1['switching_sections_23'] = 1
                    if docs['section'] == 4:
                        dict_1['switching_sections_34'] = 1
                    if docs['section'] == 5:
                        dict_1['switching_sections_45'] = 1
        #set the switching sections if entering section > exit section
        if (dict_1['entering_section'] > dict_1['exiting_section']) and dict_1['exiting_section'] != 0:
            for docs in events.find({'vehicle_no': j}):
                if docs['event_type'] == 'entering_section':
                    if docs['section'] == 2:
                        dict_1['switching_sections_32'] = 1
                    if docs['section'] == 3:
                        dict_1['switching_sections_43'] = 1
                    if docs['section'] == 4:
                        dict_1['switching_sections_54'] = 1
                    if docs['section'] == 1:
                        dict_1['switching_sections_21'] = 1
        print(dict_1)
        #predict the exiting section
        if dict_1['exiting_section'] != 0:
            actual_exit = dict_1['exiting_section']
            print(dict_1['exiting_section'])
            dict_1.pop('exiting_section')
            dict_1.pop('vehicle_no')
            
            dict_1.pop('switching_sections_12')
            dict_1.pop('switching_sections_23')
            dict_1.pop('switching_sections_34')
            dict_1.pop('switching_sections_45')
            
            dict_1.pop('switching_sections_54')
            dict_1.pop('switching_sections_43')
            dict_1.pop('switching_sections_32')
            dict_1.pop('switching_sections_21')
            
            prediction = ensemble.predict(dict_1, full=True)
            print(prediction['prediction'])
            predicted_exit = int(prediction['prediction'])
            pred_act = {}
            pred_act['vehicle_no'] = j
            pred_act['actual'] = actual_exit
            pred_act['prediction'] = predicted_exit
            predictions_actual.insert_one(pred_act)
            #create the confusion matrix 
            if actual_exit == 1:
                if predicted_exit == 1:
                    predicted_dict_1['predicted_1'] = predicted_dict_1['predicted_1'] + 1
                if predicted_exit == 2:
                    predicted_dict_1['predicted_2'] = predicted_dict_1['predicted_2'] + 1
                if predicted_exit == 3:
                    predicted_dict_1['predicted_3'] = predicted_dict_1['predicted_3'] + 1
                if predicted_exit == 4:
                    predicted_dict_1['predicted_4'] = predicted_dict_1['predicted_4'] + 1
                if predicted_exit == 5:
                    predicted_dict_1['predicted_5'] = predicted_dict_1['predicted_5'] + 1
    
            if actual_exit == 2:
                if predicted_exit == 1:
                    predicted_dict_2['predicted_1'] = predicted_dict_2['predicted_1'] + 1
                if predicted_exit == 2:
                    predicted_dict_2['predicted_2'] = predicted_dict_2['predicted_2'] + 1
                if predicted_exit == 3:
                    predicted_dict_2['predicted_3'] = predicted_dict_2['predicted_3'] + 1
                if predicted_exit == 4:
                    predicted_dict_2['predicted_4'] = predicted_dict_2['predicted_4'] + 1
                if predicted_exit == 5:
                    predicted_dict_2['predicted_5'] = predicted_dict_2['predicted_5'] + 1

            if actual_exit == 3:
                if predicted_exit == 1:
                    predicted_dict_3['predicted_1'] = predicted_dict_3['predicted_1'] + 1
                if predicted_exit == 2:
                    predicted_dict_3['predicted_2'] = predicted_dict_3['predicted_2'] + 1
                if predicted_exit == 3:
                    predicted_dict_3['predicted_3'] = predicted_dict_3['predicted_3'] + 1
                if predicted_exit == 4:
                    predicted_dict_3['predicted_4'] = predicted_dict_3['predicted_4'] + 1
                if predicted_exit == 5:
                    predicted_dict_3['predicted_5'] = predicted_dict_3['predicted_5'] + 1

            if actual_exit == 4:
                if predicted_exit == 1:
                    predicted_dict_4['predicted_1'] = predicted_dict_4['predicted_1'] + 1
                if predicted_exit == 2:
                    predicted_dict_4['predicted_2'] = predicted_dict_4['predicted_2'] + 1
                if predicted_exit == 3:
                    predicted_dict_4['predicted_3'] = predicted_dict_4['predicted_3'] + 1
                if predicted_exit == 4:
                    predicted_dict_4['predicted_4'] = predicted_dict_4['predicted_4'] + 1
                if predicted_exit == 5:
                    predicted_dict_4['predicted_5'] = predicted_dict_4['predicted_5'] + 1
    
            if actual_exit == 5:
                if predicted_exit == 1:
                    predicted_dict_5['predicted_1'] = predicted_dict_5['predicted_1'] + 1
                if predicted_exit == 2:
                    predicted_dict_5['predicted_2'] = predicted_dict_5['predicted_2'] + 1
                if predicted_exit == 3:
                    predicted_dict_5['predicted_3'] = predicted_dict_5['predicted_3'] + 1
                if predicted_exit == 4:
                    predicted_dict_5['predicted_4'] = predicted_dict_5['predicted_4'] + 1
                if predicted_exit == 5:
                    predicted_dict_5['predicted_5'] = predicted_dict_5['predicted_5'] + 1
    
    predicted['status'] = 'latest'
    predicted['section_1'] = predicted_dict_1
    predicted['section_2'] = predicted_dict_2
    predicted['section_3'] = predicted_dict_3
    predicted['section_4'] = predicted_dict_4
    predicted['section_5'] = predicted_dict_5
    
    #update the old predictions
    myquery = {}
    newvalues = { "$set": { "status": "old" } }
    x = predictions.update_many(myquery, newvalues)
    print(str(x.modified_count) +" : documents updated") 
    predictions.insert_one(predicted)
    print('predictions completed')
    time.sleep(60) #60
    myquery = {}
    x = predictions_actual.delete_many(myquery)
    print(x.deleted_count, " documents deleted.")

