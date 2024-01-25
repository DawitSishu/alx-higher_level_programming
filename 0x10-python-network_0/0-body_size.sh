#!/bin/bash
# display body
curl -so /dev/null -w '%{size_download}\n' "$1"
