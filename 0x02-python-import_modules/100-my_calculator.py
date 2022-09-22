#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    arg_num = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    oper = argv[2]

    if arg_num > 4 or arg_num <= 1:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif arg_num > 1 and arg_num == 4:
        if oper == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif oper == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif oper == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif oper == '/':
            print("{:d} / {:d} = {:.4f}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
