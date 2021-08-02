#this script consumes the messages from kafka server and loads them into redis/mongodb

import sys
import os
import json
import redis

#setting up mongodb connection

from pymongo import MongoClient
client = MongoClient("mongodb+srv://test:test@cluster0.vk3wu.mongodb.net/test?retryWrites=true&w=majority")
db = client.test
events_2 = db.events_2

#setting up redis connection

r = redis.Redis(
    host='127.0.0.1',
    port=6379)
    
#setting up kafka connection

from confluent_kafka import Consumer, KafkaException, KafkaError

if __name__ == '__main__':
    topics = os.environ['CLOUDKARAFKA_TOPIC'].split(",")

    # Consumer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    conf = {
        'bootstrap.servers': os.environ['CLOUDKARAFKA_BROKERS'],
        'group.id': "%s-consumer" % os.environ['CLOUDKARAFKA_USERNAME'],
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
	'sasl.mechanisms': 'SCRAM-SHA-256',
        'sasl.username': os.environ['CLOUDKARAFKA_USERNAME'],
        'sasl.password': os.environ['CLOUDKARAFKA_PASSWORD']
    }

    c = Consumer(**conf)
    c.subscribe(topics)
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                # Error or event
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    # Error
                    raise KafkaException(msg.error())
            else:
                # Proper message
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
                print(msg.value())
                list_1 = msg.value().decode("utf-8") 
                #list_1.replace('/','')
                list_2 = json.loads(list_1)
                vehicle = list_2["vehicle_no"]
                r.rpush(vehicle,msg.value())
                events_2.insert_one(list_2)

    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    # Close down consumer to commit final offsets.
    c.close()

