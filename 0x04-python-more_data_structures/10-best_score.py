#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_score = -99999
    key = ""

    for k, v in a_dictionary.items():
        if v >= max_score:
            max_score = v
            key = k

    return key
