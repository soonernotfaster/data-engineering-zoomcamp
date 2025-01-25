#!/usr/bin/env bash

docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v ./module_1/docker_intro/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
postgres:13 