#!/usr/bin/python3
import sys

del sys.argv[0]
argument_len = len(sys.argv)

if argument_len:
    if argument_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argument_len))

    # ...then print
    for i, arg in enumerate(sys.argv):
        print("{} : {}".format(i + 1, arg))
else:
    print("0 arguments.")
