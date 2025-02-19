import pytest
import re
from script.ingest.ingest_taxi_data import args

TABLE_ARGS = ["-t", "table_name"]
FILENAME_ARGS = ["-f", "in.csv"]
DATE_COL_ARGS = ["--date-cols", "col_a", "col_b"]

def test_all_args_missing(capsys):
    with pytest.raises(SystemExit):
        args([])
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)


def test_table_name_missing(capsys):
    with pytest.raises(SystemExit):
        args(FILENAME_ARGS)
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)

def test_filename_missing(capsys):
    with pytest.raises(SystemExit):
        args(TABLE_ARGS)
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)

def test_all_args_provided():
    result = args(TABLE_ARGS + FILENAME_ARGS + DATE_COL_ARGS)

    assert result.filename == FILENAME_ARGS[-1]
    assert result.table == TABLE_ARGS[-1]
    assert result.date_cols == DATE_COL_ARGS[1:]