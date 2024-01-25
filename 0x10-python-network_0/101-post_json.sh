#!/bin/bash
# post json body displayer
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
