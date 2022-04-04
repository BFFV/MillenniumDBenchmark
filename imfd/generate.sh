#!/bin/bash

# Prepare dir for data

rm -rf "$1_data"
mkdir "$1_data"
cd "$1_data"
mkdir workload-translated
mkdir workload-interface

# Generate graph data & internal queries (requires argument for config file name)

cd ../../src
./test -c "../imfd/config/$1.xml" -g "../imfd/$1_data/graph.txt" -w "../imfd/$1_data/workload.xml" -r "../imfd/$1_data/"

# Query translation into main syntaxes

cd querytranslate
./test -w "../../imfd/$1_data/workload.xml" -o "../../imfd/$1_data/workload-translated"

# Generate query workload interface

cd ../queryinterface
./test -w "../../imfd/$1_data/workload.xml" -t "../../imfd/$1_data/workload-translated" -o "../../imfd/$1_data/workload-interface"
