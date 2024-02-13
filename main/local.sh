#!/usr/bin/env bash

rm -rf env
python3.11 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
uvicorn main:app --reload
