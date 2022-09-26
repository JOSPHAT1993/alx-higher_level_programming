#!/usr/bin/python3
def multiple_returns(sentence):
    count = 0
    if sentence == ():
        return None
    else:
        for i in sentence:
            first = sentence[0]
            count += 1
        return count, first
