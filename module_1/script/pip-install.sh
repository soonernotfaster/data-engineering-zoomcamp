#!/usr/bin/env bash

pip install $@
python3 -m pip freeze > requirements.txt