#!/bin/bash

cd che
for file in $(find . -not -type d); do #this will break if a filename/directory contains any whitespace
    echo $file
    for email in $(git log --format=%ce -- $file); do
    	echo "${file}, ${email}" >> ../emails.txt
    done
done	
#git log --format=%ce -- $file >> ../test.txt
