#!/usr/bin/python3
"""Base Class

Todo:
    define a private class attribute nbobjects
    initialize the class with init method
"""
import json
import os.path


class Base:
    """class Base"""
    _nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string"""
        return json.dumps(list_dictionaries or [])

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file"""
        try:
            jsons = cls.to_json_string([x.to_dictionary() for x in list_objs])
        except:
            jsons = '[]'
        with open(cls.__name__+'.json', 'w', encoding='utf-8') as f:
            f.write(jsons)
