#!/usr/bin/env bash

python3.12 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload
