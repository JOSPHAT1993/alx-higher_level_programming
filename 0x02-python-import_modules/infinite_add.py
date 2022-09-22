#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = len(argv)
    add = 0
    if args > 1:
        for i in range(1, args):
            add += int(argv[i])
        print(add)
    else:
        print(add)
