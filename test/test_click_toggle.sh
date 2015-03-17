#!/bin/bash

pid=$(xprop -root | grep NDND_PID | sed -e 's/.*=//')

sleep 1
kill -USR1 $pid
