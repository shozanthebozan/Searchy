#!/bin/bash
read -p "What would you like to search for?: " query
results=$(find / \( -path "/tmp" -o -path "/proc" -o -path "/sys" -o -path "/run" \) -prune -o -iname $query -print 2> /dev/null)
if [ -z "$results" ]; then
 echo "File not found: 404"
else
 echo "$results"
fi
