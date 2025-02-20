#!/usr/bin/env bash

DEST=`mktemp`

GREEN_TRIPS_GZ="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz"
ZONES_CSV="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv"

GREEN_TRIPS_CSV=`basename -- "$GREEN_TRIPS_GZ" .gz`
echo $GREEN_TRIPS_CSV

wget $GREEN_TRIPS_GZ --directory-prefix=$DEST
wget $ZONES_CSV --directory-prefix=$DEST

echo "Data at: $DEST"

gunzip "$DEST/$(basename $GREEN_TRIPS_GZ)"

./script/ingest/ingest_taxi_data.py \
    -f "$DEST/$GREEN_TRIPS_CSV" \
    -t green_taxi_trips \
    --date-cols lpep_dropoff_datetime lpep_pickup_datetime