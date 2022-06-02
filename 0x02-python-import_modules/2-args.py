#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    if args == 0:
        print("{:d} arguments.".format(args))
    else:
        if args == 1:
            print("{:d} argument:".format(args))
        else:
            print("{:d} arguments:".format(args))
    for i in range(args):
        print("{:d}: {:s}".format(i+1, argv[i + 1]))
