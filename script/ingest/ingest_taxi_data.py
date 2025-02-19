#!/usr/bin/env python

import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, Connection
from os import PathLike
from argparse import ArgumentParser
from sys import argv

DATE_COLUMNS = ["tpep_pickup_datetime", "tpep_dropoff_datetime"]
YELLOW_CAB_CSV = "01-docker-terraform/docker_intro/data/yellow_tripdata_2021-01.csv"
ZONE_CSV = "01-docker-terraform/docker_intro/data/taxi_zone_lookup.csv"
CONNECTION_STRING = "postgresql://root:root@localhost:5432/ny_taxi"

def insert_data(connection: Connection, path: PathLike[str], table_name: str, date_columns: list[str] = None) -> None:
    """
    Inserts data in chunks from the provided path.g
    """
    data_iters = pd.read_csv(path, parse_dates=date_columns, chunksize=100_000, iterator=True)
    
    for df in tqdm(data_iters):
        df.to_sql(name=table_name, con=connection, if_exists="append")

def ingest(arguments) -> None:
    engine = create_engine(CONNECTION_STRING)
    with engine.begin() as connection:
        insert_data(connection, arguments.filename, table_name=arguments.table, date_columns = arguments.date_cols)

def args(args):
    parser = ArgumentParser(
        prog="Data ingestion",
        description="Uploads files to a postgres instance running in docker"
    )

    parser.add_argument("-f", dest="filename", required=True, help="File to ingest")
    parser.add_argument("-t", dest="table", required=True, help="Table name")
    parser.add_argument("--date-cols", dest="date_cols", required=False, help="")
    return parser.parse_args(args)

if __name__ == "__main__":
    print(argv[1:])
    arguments = args(argv[1:])
    print(arguments)
    # ingest(arguments)