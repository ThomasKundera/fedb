#!/bin/bash

# Location of this script
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd $SCRIPTDIR

echo "Setting up python environment"
# Only if runenv does not exist
if [ ! -d "runenv" ]; then
    echo "Creating runenv"
    python3 -m venv runenv
fi
source runenv/bin/activate

echo "Installing requirements"
pip install -r $SCRIPTDIR/requirements.txt

echo "Running analysis"
python $SCRIPTDIR/simple_distances.py
