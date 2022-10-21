#!/usr/bin/python3
"""5-text_indentation
   text_indentation function
"""


def text_indentation(text):
    """text indentation function
    prints a text with 2 new lines after each of these characters: . ? and :
    Args:
        text: must be a string
    Raise:
        TypeError: text must be a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for d in [".", ":", "?"]:
        text = str(d + "\n\n").join(n.strip() for n in text.split(d))

    print("{}".format(text))
