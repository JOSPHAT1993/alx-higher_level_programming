#!/usr/bin/python3
def args_add(num_args, args):
    result = 0

    if num_args > 1:
        for i in range(1, num_args):
            result += int(args[i])
    return result

if __name__ == "__main__":
    from sys import argv
    print("{:d}".format(args_add(len(argv), argv)))
