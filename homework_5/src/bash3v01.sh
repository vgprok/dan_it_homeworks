#!/bin/bash


echo -n "Enter a file name:"
read x
if [ -e "$x" ]; then
	echo "File $x exist"
else
	echo "File $x does not exist"
fi



