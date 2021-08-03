# big-data-2021

To run you need to follow these steps:

### 1- Training in BIGML:

Run:  python3 simulator_csv.py

Running the simulator creates an Excel file which we will insert into BIGML.  
In BIGML we will create a DATASET, then an ENSEMBLE .  
We will take the number ENSEMBLE and use it in prediction.  

Run:  python3 prediction_test.py  
We used this link to learn:  
 https://www.youtube.com/watch?v=zqFj6l2WZCU&list=PL1bKyu9GtNYHAk0PUojkLYZzASoYVcsTQ
  

### 2- Install NPM , Node, Redis, Pymongo  


### 3- Cleaning from a previous run and start Redis in Docker:
If you have run the code before, you should clear the data in Radis.

Run:  sudo docker stop redis-test  

Run:  sudo docker rm redis-test  
Run:  sudo docker run -d --name redis-test -p 6379:6379 -v {path}/redis.conf:/redis.conf redis redis-server /redis.conf


### 4- Run KAFKA PRODUCER  

export CLOUDKARAFKA_BROKERS="dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094"
  
export CLOUDKARAFKA_USERNAME="kvss73zm"  
  
export CLOUDKARAFKA_PASSWORD="Kr_xi43C1S12FfiJbgp3ukgbxihGG3pg"  
  
export CLOUDKARAFKA_TOPIC="kvss73zm-test"  
  
python3 test_producer.py  



### 5- Run KAFKA CONSUMER  

export CLOUDKARAFKA_BROKERS="dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094"  
  
export CLOUDKARAFKA_USERNAME="kvss73zm"  
  
export CLOUDKARAFKA_PASSWORD="Kr_xi43C1S12FfiJbgp3ukgbxihGG3pg"  
  
export CLOUDKARAFKA_TOPIC="kvss73zm-test"  

python3 test_redis_mongo_consumer.py  
  

### 6 - This script counts the vehicles from redis and loads the result into a key value in redis -- this script also gets the list of vehicles in each section
  
Run:  python3 test_python_redis.py  
  


### 7-  This script connects to mongodb and pulls the events to provide data to bigml.com for prediction. After prediction it loads the results again into mongodb to be used by node.js app  
Run:  python3 test_mongo_create_input_prediction.py  
  
NOTE:  
Please note that these python scripts will run in background,they provide data to node.js app. Have to make this python script since javascript and redis working in asynchronous mode not providing correct results with all the callbacks,promises and async/await
  
Node.js web apps : MVC architecture followed  
Python scripts : lambada model  
Redis/BigML/MongoDB : Microservices running with isolated environments  


### 8-  Creating and running the server
go to webapp directory  
run the command : npm install  
run the command server : node server  



