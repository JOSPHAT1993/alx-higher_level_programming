#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p = 0

    if (my_list):
        for i in range(x):
            try:
                print("{}".format(my_list[i]), end="")
                p += 1
            except IndexError:
                print()
                return (p)
    print()
    return (p)
