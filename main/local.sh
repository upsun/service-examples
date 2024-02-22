#!/usr/bin/env bash

ENVIRONMENT=$1
upsun tunnel:close -e $ENVIRONMENT -y
upsun tunnel:open -e $ENVIRONMENT
export PLATFORM_RELATIONSHIPS="$(upsun tunnel:info -e $ENVIRONMENT --encode)"
echo $PLATFORM_RELATIONSHIPS | base64 --decode | jq

rm -rf env
python3.11 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
# uvicorn main:app --reload
python es.py
