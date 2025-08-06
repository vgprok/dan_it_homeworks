#!/bin/bash

number=$((RANDOM % 100 + 1))

max=5
sprobi=0

echo -n "Вгадайте число від 1 до 100. Введи число:"


while [ $sprobi -lt $max ]; do

	read x
	
	sprobi=$((sprobi + 1))

	if [ "$x" -eq "$number" ]; then
		echo "Число вiрне"
	exit 0

	elif [ "$x" -lt "$number" ]; then
		echo "Надто мале число. Вводи ще раз:"
	else
		echo "Надто велико число. Води ще раз:"
	fi

	


done

echo "Вибачте, ви перевищили кількість спроб. Справжнє число було $number."


