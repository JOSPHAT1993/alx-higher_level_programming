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

try:
    json_List = load_from_json_file("add_item.json")
except:
    json_List = []

for i in sys.argv[1:]:
    json_List.append(i)
save_to_json_file(json_List, "add_item.json")
