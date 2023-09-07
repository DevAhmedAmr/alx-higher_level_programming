#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

len = len(sys.argv)

if len != 4:
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    sys.exit(1)

first_arg = int(sys.argv[1])
second_arg = int(sys.argv[3])

if sys.argv[2] == "+":
    print("{} + {} = {}".format(first_arg, second_arg, add(first_arg, second_arg)))

elif sys.argv[2] == "-":
    print("{} - {} = {}".format(first_arg, second_arg, sub(first_arg, second_arg)))

elif sys.argv[2] == "*":
    print("{} * {} = {}".format(first_arg, second_arg, mul(first_arg, second_arg)))

elif sys.argv[2] == "/":
    print("{} / {} = {}".format(first_arg, second_arg, div(first_arg, second_arg)))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
