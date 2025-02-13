#!/usr/bin/env bash

# Aliases
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Virtual env
VENV_PATH=data-camp/bin
ACTIVATION_FILE=$VENV_PATH/activate

if [[ -f ACTIVATION_FILE ]]; then
    source $ACTIVATION_FILE
else
    echo "Creating new venv"
    python3 -m venv $VENV_PATH
fi