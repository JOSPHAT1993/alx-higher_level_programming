#!/usr/bin/python3
"""4-from_json_string

Todo:
    returns data structure repr by JSON String
"""
import json


def from_json_string(my_str):
    """loading from json file"""
    return json.loads(my_str)
