#!/bin/bash


echo "Some text" > somefile9.txt

x=somefile9.txt

if [[ -f "$x" ]]; then

	echo -n "File '$x' contains:"
	cat "$x"

else
	echo "Error"
fi





