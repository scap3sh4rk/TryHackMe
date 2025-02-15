#!/bin/bash

# Loop through values from 1 to 100
for i in {0..100}
do
  # Fetch the response for each value
  echo "Fetching response for note=$i"
  curl "http://10.10.144.57/note.php?note=$i"
  echo -e "\n----------------------------\n"
done
