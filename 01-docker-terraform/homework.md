# Module 1 Homework

## Question 1

The interactive mode isn't needed but executing `docker run python:3.12.8 pip --version` shows that pip version is: `24.3.1`.

## Question 2

The `pgadmin` service can use the `hostname` of `db` and the `port` `5433` within the default network that has been created.

A connection string for the `pgadmin` service would be `postgres://db:5433`. The container name `postgres` may also be used as the `hostname`.

## Question 3

I have generalized the upload script at `script/ingest/taxi_data.sh` to allow for the upload of the zone and green taxi data for this exercise.

The word "respectively" hints that there is a categorical way to slice this data.

The categorical variable is the one defined by the prompt. I am not clear why there are five rows of output in the homework document though.

```sql
WITH 
	october_trips AS (
		SELECT * FROM green_taxi_trips
		WHERE 
			lpep_dropoff_datetime >= '2019-10-01' AND lpep_dropoff_datetime < '2019-11-01'
			AND lpep_pickup_datetime >= '2019-10-01' AND lpep_pickup_datetime < '2019-11-01'
	)
	, distance_types AS (
		SELECT 
			index, 
			CASE
				WHEN "trip_distance" <= 1 THEN '1 mile or less'
				WHEN "trip_distance" > 1 AND "trip_distance" <= 3 THEN '1~3 miles'
				WHEN "trip_distance" > 3 AND "trip_distance" <= 7 THEN '3~7 miles'
				WHEN "trip_distance" > 7 AND "trip_distance" <= 10 THEN '7~10 miles'
				WHEN "trip_distance" > 10 THEN 'Over 10 miles'
			END distance_cat
		FROM october_trips
	)

SELECT 
	to_char(COUNT(index), '999,999'), distance_cat 
FROM distance_types
GROUP BY distance_cat
```

