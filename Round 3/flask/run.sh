#!/bin/bash
export FLASK_APP=app.py
export FLASK_ENV=development
. ./venv/bin/activate
cd ./tiger
flask run
