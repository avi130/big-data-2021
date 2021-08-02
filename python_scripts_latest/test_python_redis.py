#this script connects to redis db and gets the no of vehicles in each section of toll road

import redis
import json
import time

#set up redis connection

r = redis.Redis(
    host='127.0.0.1',
    port=6379)

#create a continuous loop to run in background

while(1 == 1):
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    v5 = 0
    r.delete("list_section_1")
    r.delete("list_section_2")
    r.delete("list_section_3")
    r.delete("list_section_4")
    r.delete("list_section_5")
    #get total vehicles from redis db
    vehicles_total_1 = r.get('vehicles_total')
    vehicles_total = int(vehicles_total_1.decode("utf-8"))
    print(vehicles_total)
    #loop over the total no of vehicles
    for i in range(100001, vehicles_total):
        res = r.lrange(i, -1, -1)
        res = res[0]
        res = res.decode("utf-8")
        j = json.loads(res)
        print(j)
        print(j["section"])
        s = int(j["section"])
        v = j["vehicle_no"]
        c = j["car_type"]
        e = j["event_type"]
        v = str(v) + " : " + c
        #increase the count of section 1 if section is 1 from the redis db
        #add to section 1 set
        if s == 1 and e != 'exiting_road':
            v1 += 1
            r.sadd("list_section_1", v)
        #increase the count of section 1 if section is 1 from the redis db
        #add to section 2 set
        if s == 2 and e != 'exiting_road':
            v2 += 1
            r.sadd("list_section_2", v)
        #increase the count of section 1 if section is 1 from the redis db
        #add to section 3 set
        if s == 3 and e != 'exiting_road':
            v3 += 1
            r.sadd("list_section_3", v)
        #increase the count of section 1 if section is 1 from the redis db
        #add to section 4 set
        if s == 4 and e != 'exiting_road':
            v4 += 1
            r.sadd("list_section_4", v)
        #increase the count of section 1 if section is 1 from the redis db
        #add to section 5 set
        if s == 5 and e != 'exiting_road':
            v5 += 1
            r.sadd("list_section_5", v)
    #set the no of vehicles in redis db key value
    r.set('section_1', v1)
    r.set('section_2', v2)
    r.set('section_3', v3)
    r.set('section_4', v4)
    r.set('section_5', v5)
    v = {"v1":v1,"v2":v2,"v3":v3,"v4":v4,"v5":v5}
    v = json.dumps(v)
    r.set('sections_vehicles_nos',v)
    print('updated no of vehicles in each section')
    print('updated list of vehicles in each section')
    time.sleep(60)
