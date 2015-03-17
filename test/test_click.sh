#!/bin/bash

pid=$(xprop -root | grep NDND_PID | sed -e 's/.*=//')
echo $pid

while true; do
    sleep 2
    kill -USR1 $pid
done
