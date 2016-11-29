#!/bin/bash

# Build Docker images
docker build -t myspark:2.0 ./

# start the container
docker run -it -p 8088:8088 -p 8042:8042 -p 4040:4040 -h sandbox myspark:2.0 bash

# run the code inside the container
cd /usr/local/spark
./bin/spark-submit bigram.py 
