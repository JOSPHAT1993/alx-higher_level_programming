#!/usr/bin/python3
"""5-save_to_json_file

Todo:
    writing to a json file
"""
import json


def save_to_json_file(my_obj, filename):
    """writes on json file"""
    with open(filename, mode='w', encoding="UTF-8") as f:
        f.write(json.dumps(my_obj))
