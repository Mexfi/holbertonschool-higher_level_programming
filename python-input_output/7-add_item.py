#!/usr/bin/python3
"""
Script that adds command-line arguments to a Python list and saves
the list in a JSON file named add_item.json.

Uses:
    - save_to_json_file() from 5-save_to_json_file.py
    - load_from_json_file() from 6-load_from_json_file.py

The file is created if it does not exist.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except Exception:
    data = []

data.extend(sys.argv[1:])

save_to_json_file(data, filename)
