#!/bin/bash

# Build Docker images
docker build -t sparkimg:2.0 ./

# start the container
#docker run -it -p 8088:8088 -p 8042:8042 -p 4040:4040 -h sandbox sparkimg:2.0 --name myspark bash
docker run -d --name myspark sparkimg:2.0
sleep 10
# run the code inside the container
#cd /usr/local/spark/
echo "start run python doc"
<<<<<<< HEAD
docker exec myspark /bin/spark-submit /usr/local/spark/bigram.py
=======
docker exec myspark ./bin/spark-submit /usr/local/spark/bigram.py
>>>>>>> fc6b7614ac7ad648b89ef2eba32491148fc4cd33

#echo the result
docker exec myspark cat /usr/local/spark/output/part-00000
docker exec myspark cat /usr/local/spark/result.txt

#Clean
docker stop myspark
docker rm myspark
