#!/usr/bin/python3
"""1-my_list

Todo:
    creates a sub class(Mylist) of class(list)
    prints sorted values in the list
"""
class MyList(list):
    """prints a sorted list"""
    def print_sorted(self):
        print(sorted(self))
