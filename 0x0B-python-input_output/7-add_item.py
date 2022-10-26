#!/usr/bin/python3
"""7-add_item

Todo:
    add item in a json file
    save it and
    load the file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv
filename = "add_item.json"
with open(filename, mode='a+', encoding="UTF-8") as f:
    my_list = []
    my_list.extend(args[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
