#!/usr/bin/python3
if __name__ == "__main__":
    import sys

n = len(sys.argv)

if n < 2:
    print("{} arguments.".format(n-1))
elif n==2:
    print("1 argument: ",sys.argv[1]) 
else:
    print("{} arguments:".format(n-1))
    for i in range(1, n):
        print("{}: {}".format(i, sys.argv[i]))
