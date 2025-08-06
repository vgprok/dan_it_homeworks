#!/bin/bash


touch testfile


a() {
	mkdir $1 $2
}

a dir1 dir2

echo -n "Select file to copy:"
read x

if [ "$x" = "testfile" ]; 
then 
	cp $x dir1/ 
	cp $x dir2/

else
	echo "Denied"
fi
	
	
