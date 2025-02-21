# Module 1 Homework

## Question 1

The interactive mode isn't needed but executing `docker run python:3.12.8 pip --version` shows that pip version is: `24.3.1`.

## Question 2

The `pgadmin` service can use the `hostname` of `db` and the `port` `5433` within the default network that has been created.

A connection string for the `pgadmin` service would be `postgres://db:5433`. The container name `postgres` may also be used as the `hostname`.

## Question 3

I have generalized the upload script at `script/ingest/taxi_data.sh` to allow for the upload of the zone and green taxi data for this exercise.

The word "respectively" hints that there is a categorical way to slice this data.