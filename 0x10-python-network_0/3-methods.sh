#!/bin/bash
# http accept displayer
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
