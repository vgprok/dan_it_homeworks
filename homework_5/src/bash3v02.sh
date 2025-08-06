#!/bin/bash

x() {
       if [ -e "/home/vvppnko/dan_it_homeworks/homework_5/src/$1" ]; then
return 0

else
	return 1
       fi
}

echo -n "Enter file name:"
read name
x "$name"

if [ $? -eq 0 ]; then 
	echo "File found"
else
	echo "File dosent found"
fi
