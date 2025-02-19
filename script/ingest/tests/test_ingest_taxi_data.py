import pytest
import re
from script.ingest.ingest_taxi_data import args

def test_all_args_missing(capsys):
    with pytest.raises(SystemExit):
        args([])
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)


def test_table_name_missing(capsys):
    with pytest.raises(SystemExit):
        args(["-f", "in.csv"])
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)

def test_filename_missing(capsys):
    with pytest.raises(SystemExit):
        args(["-t", "table_name"])
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)

def test_all_args_provided():
    result = args(["-f", "in.csv", "-t", "table_name"])

    assert result.filename == "in.csv"
    assert result.table == "table_name"