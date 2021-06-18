#!/bin/bash

xhost +
docker run --device /dev/video0 -it -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD:/app server /bin/bash
