#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        for key, val in sorted(dict.items(a_dictionary)):
            print("{} : {}".format(key, val))
