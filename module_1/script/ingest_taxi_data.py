#!/usr/bin/env python

import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, Engine, Connection
from os import PathLike

DATE_COLUMNS = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
INPUT_PATH = "module_1/docker_intro/data/yellow_tripdata_2021-01.csv"
CONNECTION_STRING = "postgresql://root:root@localhost:5432/ny_taxi"
TABLE_NAME = "yellow_taxi_data"

def insert_data(connection: Connection, path: PathLike[str]) -> None:
    """
    Inserts data in chunks from the provided path.
    """
    data_iters = pd.read_csv(path, parse_dates=DATE_COLUMNS, chunksize=100_000, iterator=True)
    
    for df in tqdm(data_iters):
        df.to_sql(name=TABLE_NAME, con=connection, if_exists="append")

def ingest() -> None:
    engine = create_engine(CONNECTION_STRING)
    with engine.begin() as connection:
        insert_data(connection, INPUT_PATH)

if __name__ == "__main__":
    ingest()