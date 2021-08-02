#This script acts as a simulator of vehicles in toll road section
#Also this script generates messages for kafka server in cloud

import time
import asyncio
import sys
import os
import redis
from confluent_kafka import Producer
from random import choices

#setting up kafka environment details

topic = os.environ['CLOUDKARAFKA_TOPIC'].split(",")[0]
conf = {
    'bootstrap.servers': os.environ['CLOUDKARAFKA_BROKERS'],
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'},
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'SCRAM-SHA-256',
    'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
    'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD']
}


p = Producer(**conf)

#setting up redis connection details

r = redis.Redis(
    host='127.0.0.1',
    port=6379)

#this function is passed as callback to the kafka producer, callback functions get executed after the main function finishes

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d]\n' % (msg.topic(), msg.partition()))

#this function creates json and calls the producer to kafka

def produce_json(json_msg):
    try:
        p.produce(topic, json_msg, callback=delivery_callback)
    except BufferError as e:
        sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' % len(p))
    p.poll(0)
    sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
    p.flush()

#this is the function that acts as the simulator
#when the vehicle can enter in any one of the sections from 1 to 5
#if section 1 : it makes switches (1 to 2,2 to 3,3 to4,4 to 5) or can exit from any section
#if section 2 : it makes switches (2 to 3, 3 to 4, 4 to 5) or can exit from any section
#if section 3 : it makes switches (3 to 4, 4 to 5) or can exit from any section
#if section 4 : it makes switches (4 to 5) or can exit from any section
#it will make the entry and exit section random(exit >= entry)

#when the vehicle can enter in any one of the sections from 5 to 1
#if section 5 : it makes switches (5 to 4,4 to 3,3 to 2,2 to 1) or can exit from any section
#if section 4 : it makes switches (4 to 3, 3 to 2, 2 to 1) or can exit from any section
#if section 3 : it makes switches (3 to 2, 2 to 1) or can exit from any section
#if section 2 : it makes switches (2 to 1) or can exit from any section
#it will make the entry and exit section random(exit <= entry)

async def simulator_vehicle(i):
    import datetime
    import random
    import json
    vehicle_no = i
    list_car_type = ['private', 'van', 'truck']
    list_event_type = ['entering road', 'entering section', 'exiting road', 'exiting section']
    list_special_day = ['YES', 'NO']
    car_type = random.uniform(1, 3)
    special_day = random.uniform(1, 2)
    event = 'entering road'
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
    switching_sections = round(random.uniform(0, 4))
    day = datetime.date.today()
    now = datetime.datetime.now()
    current_time = now.strftime("%H")
    #current_day = day.strftime("%m")
    current_day = day.weekday() + 1
    
    # entering road event
    event_entering_road = {}
    event_entering_road['vehicle_no'] = vehicle_no
    event_entering_road['event_type'] = 'entering_road'
    event_entering_road['section'] = entering_section
    # event_entering_road['exiting_section'] = entering_section
    event_entering_road['car_type'] = list_car_type[round(car_type) - 1]
    event_entering_road['day'] = current_day
    event_entering_road['hour'] = current_time
    event_entering_road['special_day'] = list_special_day[round(special_day) - 1]
    json_data = json.dumps(event_entering_road)
    print(json_data)
    produce_json(json_data)
    await asyncio.sleep(90)
    if exiting_section > entering_section:
        switching_sections = exiting_section - entering_section
        entering_section_1 = entering_section
        for i in range(1, switching_sections + 1):
            day = datetime.date.today()
            now = datetime.datetime.now()
            #current_day = day.strftime("%m")
            current_day = day.weekday() + 1
            current_time = now.strftime("%H")
            event_1 = {}
            # event_1['entering_section'] = entering_section
            event_1['vehicle_no'] = vehicle_no
            event_1['event_type'] = 'exiting_section'
            event_1['section'] = entering_section_1
            event_1['car_type'] = list_car_type[round(car_type) - 1]
            event_1['day'] = current_day
            event_1['hour'] = current_time
            event_1['special_day'] = list_special_day[round(special_day) - 1]
            json_data = json.dumps(event_1)
            print(json_data)
            produce_json(json_data)
            await asyncio.sleep(10)
            event_2 = {}
            event_2['vehicle_no'] = vehicle_no
            event_2['event_type'] = 'entering_section'
            event_2['section'] = entering_section_1 + 1
            # event_2['exiting_section'] = entering_section+1
            event_2['car_type'] = list_car_type[round(car_type) - 1]
            event_2['day'] = current_day
            event_2['hour'] = current_time
            event_2['special_day'] = list_special_day[round(special_day) - 1]
            json_data = json.dumps(event_2)
            print(json_data)
            produce_json(json_data)
            await asyncio.sleep(90)
            entering_section_1 = entering_section_1 + 1

    if exiting_section < entering_section:
        switching_sections = entering_section - exiting_section
        entering_section_1 = entering_section
        for i in range(1, switching_sections + 1):
            day = datetime.date.today()
            now = datetime.datetime.now()
            #current_day = day.strftime("%m")
            current_day = day.weekday() + 1
            current_time = now.strftime("%H")
            event_1 = {}
            # event_1['entering_section'] = entering_section
            event_1['vehicle_no'] = vehicle_no
            event_1['event_type'] = 'exiting_section'
            event_1['section'] = entering_section_1
            event_1['car_type'] = list_car_type[round(car_type) - 1]
            event_1['day'] = current_day
            event_1['hour'] = current_time
            event_1['special_day'] = list_special_day[round(special_day) - 1]
            json_data = json.dumps(event_1)
            print(json_data)
            produce_json(json_data)
            await asyncio.sleep(10)
            event_2 = {}
            event_2['vehicle_no'] = vehicle_no
            event_2['event_type'] = 'entering_section'
            event_2['section'] = entering_section_1 - 1
            # event_2['exiting_section'] = entering_section+1
            event_2['car_type'] = list_car_type[round(car_type) - 1]
            event_2['day'] = current_day
            event_2['hour'] = current_time
            event_2['special_day'] = list_special_day[round(special_day) - 1]
            json_data = json.dumps(event_2)
            print(json_data)
            produce_json(json_data)
            await asyncio.sleep(90)
            entering_section_1 = entering_section_1 - 1

    # exiting road event
    event_exiting_road = {}
    event_exiting_road['vehicle_no'] = vehicle_no
    event_exiting_road['event_type'] = 'exiting_road'
    event_exiting_road['section'] = exiting_section
    # event_entering_road['exiting_section'] = entering_section
    event_exiting_road['car_type'] = list_car_type[round(car_type) - 1]
    event_exiting_road['day'] = current_day
    event_exiting_road['hour'] = current_time
    event_exiting_road['special_day'] = list_special_day[round(special_day) - 1]
    json_data = json.dumps(event_exiting_road)
    print(json_data)
    produce_json(json_data)
    # await asyncio.sleep(60)

#this function will run in loop to simulate the vehicles

async def main():
    v=100000
    while True:
        v = v + 1
        r.set('vehicles_total',v)   
        asyncio.ensure_future(simulator_vehicle(v))
        await asyncio.sleep(10)
        


asyncio.run(main())

