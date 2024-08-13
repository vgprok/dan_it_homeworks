#!/bin/bash

textfile="textfile"


for a in 1 2 3 4 5 6 7 8 9 10
do 
	echo "some text $a" >> "textfile"
done



r=$(wc -l < "textfile")




echo "Количество строк: $r"


