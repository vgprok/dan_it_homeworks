#!/bin/bash

x=50

usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')




y="/var/log/disk.log"

if [ "$x" -gt "$usage" ]; then
	echo "Використання простору в кореневому роздiлi $usage" >> $y

fi



