#!/bin/bash
read -p "What would you like to search for?: " query
results=$(find / -name $query 2> /dev/null)
if [ -z "$results" ]; then
 echo "File not found: 404"
else
 echo "$results"
fi
