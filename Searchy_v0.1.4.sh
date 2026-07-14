#!/bin/bash
read -p "What would you like to search for?: " query
read -p "Which directory would you like to search in? (default=/): " search_dir
if [ -z "$search_dir" ]; then
 search_dir="/"
else
 search_dir=$"search_dir"
fi
results=$(find "$search_dir" \( -path "/tmp" -o -path "/proc" -o -path "/sys" -o \( -path "/run/*" -not -path "/run/media*" \) \) -prune -o -iname "$query" -print 2> /dev/null)
if [ -z "$results" ]; then
 echo "File not found: 404"
else
 echo "$results"
fi
