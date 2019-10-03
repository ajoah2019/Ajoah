#!/bin/sh

echo Good

APPNAME=ajoah
APP_DIR=/var/etc/MyData
REVISION=$(expr substr $(git rev-parse HEAD) 1 7)

docker build --tag $APPNAME:$REVISION .
docker stop $APPNAME
docker rm $APPNAME
docker run -d --name $APPNAME -p 80:80 $APPNAME:$REVISION

