#!/bin/bash
echo cd /data
echo /entrypoint.sh redis-server 
docker run --name=db2 -t -i --rm -v `pwd`/../data:/data powellquiring/pdb2:1.0 /bin/bash
