#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

num_args = len(argv)
if num_args == 1:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(num_args - 1))
    for i in range(num_args - 1):
        print("{:d} : {}".format(i + 1, argv[i + 1]))
