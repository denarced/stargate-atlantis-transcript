#!/bin/bash

# Create the directory if it does not exist
if [ ! -d re-encoded ]
then
    mkdir re-encoded/
fi

for each in `find origs -type f | sort`
do
    filename=`basename $each`
    dest="re-encoded/$filename"
    echo "$each; $filename; $dest"
    iconv -f WINDOWS-1252 -t UTF-8 -o $dest $each
done
