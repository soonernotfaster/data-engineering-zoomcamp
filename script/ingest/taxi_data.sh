#!/usr/bin/env bash

DEST=`mktemp`

GREEN_TRIPS="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"
ZONES="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

wget $GREEN_TRIPS --directory-prefix=$DEST
wget $ZONES --directory-prefix=$DEST

echo "Data at: $DEST"

gunzip "$DEST/$(basename $GREEN_TRIPS)"

./01-docker-terraform/script/ingest_taxi_data.py -f 01-docker-terraform/docker_intro/data/taxi_zone_lookup.csv  -t wobb