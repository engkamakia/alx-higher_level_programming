#!/usr/bin/python3

if __name__ == "__main__":  
    import sys

    no_of_args = len(sys.argv) - 1
    if no_of_args == 0:
        print("0 arguments.")
    elif no_of_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(no_of_args))
    for i in range(no_of_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))