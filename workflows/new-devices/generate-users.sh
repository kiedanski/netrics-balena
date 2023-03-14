#!/usr/bin/env bash
touch users.csv
for i in $(seq 1 20); do
    name=$(gpw 1 15)
    uuid=$(uuidgen | tr -d "-")
    version=$((($RANDOM % 2) + 3)) # modify to reflect actual deployment in the future
    echo "$name,$uuid,$version" >> users.csv
done