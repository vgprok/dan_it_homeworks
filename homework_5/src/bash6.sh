#!/bin/bash



rev=$(echo "Hello World" | awk '{for(i=NF;i>0;i--) printf "%s ", $i; print ""}')

echo "$rev"

