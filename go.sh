#!/bin/bash

# Build Docker images
docker build -t sparkimg:2.0 ./

# start the container
#docker run -it -p 8088:8088 -p 8042:8042 -p 4040:4040 -h sandbox sparkimg:2.0 --name myspark bash
docker run -it --name myspark sparkimg:2.0 /bin/bash /usr/local/spark/startBigram.sh


#Clean
docker stop myspark
docker rm myspark
