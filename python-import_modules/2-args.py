#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    count = len(argv) - 1

    if count == 0:
        print("0 arguments.")
    else:
        word = "argument" if count == 1 else "arguments"
        print("{} {}:".format(count, word))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
