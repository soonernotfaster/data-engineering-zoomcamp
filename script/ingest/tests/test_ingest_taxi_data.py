import pytest
import re
from script.ingest.ingest_taxi_data import args

TABLE_ARGS = ["-t", "table_name"]
FILENAME_ARGS = ["-f", "in.csv"]
DATE_COL_ARGS = ["--date-cols", "col_a", "col_b"]

FILENAME_FLAG = "-f"
TABLE_FLAG = "-t"

@pytest.mark.parametrize(
        ("input", "pattern"),
        [
            pytest.param([], f".*required:", id="no args"),
            pytest.param(TABLE_ARGS, f".*required:.*{FILENAME_FLAG}.*", id="missing filename args"),
            pytest.param(FILENAME_ARGS, f".*required:.*{TABLE_FLAG}.*", id="missing table args"),
        ]
)
def test_incomple_args(capsys, input, pattern):
    with pytest.raises(SystemExit):
        args(input)
    
    _out, err = capsys.readouterr()
    assert re.match(pattern, err, flags=re.MULTILINE | re.DOTALL)

def test_all_args_provided():
    result = args(TABLE_ARGS + FILENAME_ARGS + DATE_COL_ARGS)

    assert result.filename == FILENAME_ARGS[-1]
    assert result.table == TABLE_ARGS[-1]
    assert result.date_cols == DATE_COL_ARGS[1:]