import pytest
import re
from script.ingest.ingest_taxi_data import args

def test_args(capsys):
    with pytest.raises(SystemExit):
        args("")
    
    _out, err = capsys.readouterr()
    assert re.match("usage:.*", err)