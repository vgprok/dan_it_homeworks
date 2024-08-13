#!/bin/bash

watchdir=/home/vvppnko/watch

inotifywait -m -e create --format '%f' "$watchdir" | while read NEW_FILE


do

	path="$watchdir/$NEW_FILE"
	path2="$path.back"


	echo "New file found: $NEW_FILE"

	mv "$path" "$path2"
	echo "New name:$path2"
done





