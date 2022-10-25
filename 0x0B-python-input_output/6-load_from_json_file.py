#!/usr/bin/python3
"""6-load_from_json_file

Todo:
    Create an object from json file i.e.
    convert a json file to object file
"""
import json


def load_from_json_file(filename):
    with open(filename, mode='r', encoding="UTF-8") as f:
        return json.load(f)
