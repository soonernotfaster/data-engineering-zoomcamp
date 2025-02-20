#!/usr/bin/env python

import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, Connection, text, String
from os import PathLike
from argparse import ArgumentParser
from sys import argv

CONNECTION_STRING = "postgresql://root:root@localhost:5432/ny_taxi"

def insert_data(connection: Connection, path: PathLike[str], table_name: str, date_columns: list[str] = None) -> None:
    """
    Inserts data in chunks from the provided path.
    """
    data_iters = pd.read_csv(path, parse_dates=date_columns, chunksize=100_000, iterator=True)
    
    for df in tqdm(data_iters):
        df.to_sql(name=table_name, con=connection, if_exists="append")

def drop_table(connection: Connection, table_name: str) -> None:
    """Drops the table if it exists"""
    # Unfortunality, there is no way to parameterize the table in a safe way
    drop_command = text(f"DROP TABLE IF EXISTS {table_name};")
    connection.execute(drop_command)

def load(input) -> None:
    """drops table and loads in a fresh copy"""
    engine = create_engine(CONNECTION_STRING)
    with engine.begin() as connection:
        drop_table(connection, input.table)
        insert_data(connection, input.filename, table_name=input.table, date_columns = input.date_cols)

def parse_input(args):
    """Parses commandline arguments into an object"""
    parser = ArgumentParser(
        prog="Data ingestion",
        description="Uploads files to a postgres instance running in docker"
    )

    parser.add_argument("-f", dest="filename", required=True, help="File to ingest")
    parser.add_argument("-t", dest="table", required=True, help="Table name")
    parser.add_argument("--date-cols", dest="date_cols", nargs="*", required=False, help="")
    return parser.parse_args(args)

if __name__ == "__main__":
    input = parse_input(argv[1:])
    load(input)