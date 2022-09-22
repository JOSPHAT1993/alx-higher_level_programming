#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    num_args = len(argv)
    if num_args == 1:
        print("{:d} arguments.".format(num_args - 1))
    elif num_args == 2:
        print("{:d} argument:".format(num_args - 1))
        print("{:d} {}".format(num_args - 1, argv[num_args - 1]))
    else:
        print("{:d} arguments:".format(num_args - 1))
        for i in range(1, num_args):
            print("{:d} : {}".format(i, argv[i]))
