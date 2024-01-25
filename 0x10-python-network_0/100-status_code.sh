#!/bin/bash
# status code displayer
curl -so /dev/null -w '%{http_code}' "$1"
