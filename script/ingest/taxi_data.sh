#!/usr/bin/env bash

DEST=`mktemp`

GREEN_TRIPS_SOURCE="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"
ZONES_SOURCE="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"
YELLOW_TRIPS_SOURCE="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

function csv_for_trip() {
    local DEST=$1
    local TRIP_SOURCE=$2
    local FILE_OUTPUT=`basename -- "$TRIP_SOURCE" .gz`

    wget $TRIP_SOURCE --directory-prefix=$DEST

    gunzip "$DEST/$(basename $TRIP_SOURCE)"
    
    echo $FILE_OUTPUT
}

GREEN_TRIPS_CSV=$(csv_for_trip $DEST $GREEN_TRIPS_SOURCE)
YELLOW_TRIPS_CSV=$(csv_for_trip $DEST $YELLOW_TRIPS_SOURCE)

wget $ZONES_SOURCE --directory-prefix=$DEST
ZONES_CSV=`basename $ZONES_SOURCE`

echo "Data at: $DEST"

./script/ingest/load_into_database.py \
    -f "$DEST/$GREEN_TRIPS_CSV" \
    -t green_taxi_trips \
    --date-cols lpep_dropoff_datetime lpep_pickup_datetime

./script/ingest/load_into_database.py \
    -f "$DEST/$ZONES_CSV" \
    -t taxi_zones

./script/ingest/load_into_database.py \
    -f "$DEST/$YELLOW_TRIPS_CSV" \
    -t yellow_taxi_trips \
    --date-cols tpep_pickup_datetime tpep_dropoff_datetime