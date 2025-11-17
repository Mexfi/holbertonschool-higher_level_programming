#!/usr/bin/python3
import sys

def add_arguments():
    """
    Calculates the sum of all command-line arguments, treating them as integers.
    Prints the result followed by a new line.
    """
    total_sum = 0
    # sys.argv[0] is the script name, so we start from index 1 for arguments.
    for arg in sys.argv[1:]:
        total_sum += int(arg)
    print(total_sum)

if __name__ == "__main__":
    add_arguments()
