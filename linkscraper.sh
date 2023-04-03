#!/bin/bash

base_url="https://jadi.net/tag/podcast/page/"
num_pages=50
page=1

while [ $page -le $num_pages ]
do
    url="$base_url$page/"
    response=$(curl -s -o /dev/null -w "%{http_code}" $url)

    if [ $response -eq 404 ]
    then
        echo "Page $page not found. Stopping the loop."
        break
    fi

    html_content=$(curl -s $url)
    mp3_links=$(echo "$html_content" | grep -Eo '"(http|https)://.*\.mp3"' | sed 's/"//g')

    echo "$mp3_links" >> links-sh

    page=$((page + 1))
done

