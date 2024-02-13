#!/usr/bin/env bash

ENVIRONMENT=$1
upsun tunnel:close -e $ENVIRONMENT -y
upsun tunnel:open -e $ENVIRONMENT
export PLATFORM_RELATIONSHIPS="$(upsun tunnel:info -e $ENVIRONMENT --encode)"
