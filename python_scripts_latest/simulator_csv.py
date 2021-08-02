#this script creates the csv file for training to be uploaded in BigML

import datetime
import random
import csv
from random import choices

def simulator_vehicle_training(v):
    vehicle_no = v
    list_car_type=['private','van','truck']
    list_event_type=['entering road','entering section','exiting road','exiting section']
    list_special_day = ['YES','NO']
    car_type = random.uniform(1,3)
    special_day = random.uniform(1,2)
    event='entering road'
    entering_section = int(round(random.uniform(1,5)))
    if(entering_section == 1):
    	population = [1, 2, 3, 4, 5]
    	weights = [1, 1, 1, 8, 1]
    	exiting_section = choices(population, weights)
    	exiting_section = exiting_section[0]
    elif(entering_section == 2):
    	population = [1, 2, 3, 4, 5]
    	weights = [1, 1, 8, 1, 1]
    	exiting_section = choices(population, weights)
    	exiting_section = exiting_section[0]
    elif(entering_section == 3):
    	population = [1, 2, 3, 4, 5]
    	weights = [1, 1, 1, 1, 8]
    	exiting_section = choices(population, weights)
    	exiting_section = exiting_section[0]
    elif(entering_section == 4):
    	population = [1, 2, 3, 4, 5]
    	weights = [8, 1, 1, 1, 1]
    	exiting_section = choices(population, weights)
    	exiting_section = exiting_section[0]
    else:
    	population = [1, 2, 3, 4, 5]
    	weights = [1, 8, 1, 1, 1]
    	exiting_section = choices(population, weights)
    	exiting_section = exiting_section[0]
    #exiting_section = round(random.uniform(1,5))
    print(entering_section)
    print(exiting_section)
    day = datetime.date.today()
    now = datetime.datetime.now()
    #current_time = now.strftime("%H")
    #days_to_subtract = round(random.uniform(1,100))
    hours_to_subtract = round(random.uniform(1,24))
    #current_day = (day - datetime.timedelta(days=days_to_subtract)).strftime('%m')
    current_day = round(random.uniform(1,7))
    current_time = hours_to_subtract
    list_csv = []
    list_csv.append(list_car_type[round(car_type)-1])
    list_csv.append(list_special_day[round(special_day)-1])
    list_csv.append(current_day)
    list_csv.append(current_time)
    list_csv.append(entering_section)
    list_csv.append(exiting_section)
    #print(list_csv)
    return list_csv

fields = ['vehicle_type','special_day','day','hour','entering_section','exiting_section']
filename = "training_data.csv"
csvfile = open(filename, 'w')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)
    
for i in range(1,101):
    list_csv_1 = simulator_vehicle_training(i)
    print(list_csv_1)
    csvwriter.writerow(list_csv_1)
