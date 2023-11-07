#!/usr/bin/python3
"""
a script to add all arguments to a file
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


file = "add_item.json"

try:
    jsons = load_from_json_file(file)
except Exception:
    jsons = []
for arg in argv[1:]:
    jsons.append(arg)
save_to_json_file(jsons, file)
