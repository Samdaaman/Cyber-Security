#!/bin/bash
cd "`dirname "$0"`" #use the dir that the script is in
echo "Using dir `pwd`"
rm -rf venv
before=`which python`
python3 -m venv venv
. venv/bin/activate
after=`which python`
if [ "$before" == "$after" ]; then
    echo "Couldn't setup python venv, is venv installed?"
    exit
else
    echo "Python env changed"
fi
echo "Installing requirements"
echo
sleep 1
pip install -r requirements.txt
sleep 1
echo
echo "Done"
