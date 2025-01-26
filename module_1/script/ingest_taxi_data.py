#!/usr/bin/env python

import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, Engine, Connection
from os import PathLike

DATE_COLUMNS = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
YELLOW_CAB_CSV = "module_1/docker_intro/data/yellow_tripdata_2021-01.csv"
ZONE_CSV = "module_1/docker_intro/data/taxi_zone_lookup.csv"
CONNECTION_STRING = "postgresql://root:root@localhost:5432/ny_taxi"

def insert_data(connection: Connection, path: PathLike[str], table_name: str, date_columns: list[str] = None) -> None:
    """
    Inserts data in chunks from the provided path.g
    """
    data_iters = pd.read_csv(path, parse_dates=date_columns, chunksize=100_000, iterator=True)
    
    for df in tqdm(data_iters):
        df.to_sql(name=table_name, con=connection, if_exists="append")

def ingest() -> None:
    engine = create_engine(CONNECTION_STRING)
    with engine.begin() as connection:
        insert_data(connection, YELLOW_CAB_CSV, table_name="yellow_taxi_data", date_columns = DATE_COLUMNS)
        insert_data(connection, ZONE_CSV, table_name="zone")

if __name__ == "__main__":
    ingest()