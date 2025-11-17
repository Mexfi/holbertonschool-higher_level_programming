#!/usr/bin/python3
import sys

def print_arguments():
    """
    Prints the number of and the list of command-line arguments.
    Excludes the script name itself from the count and list.
    """
    args = sys.argv[1:]  # Exclude the script name (sys.argv[0])
    num_args = len(args)

    if num_args == 0:
        print("0 arguments.")
    else:
        argument_word = "argument" if num_args == 1 else "arguments"
        print(f"{num_args} {argument_word}:")
        for i, arg in enumerate(args):
            print(f"{i + 1}:{arg}")

if __name__ == "__main__":
    print_arguments()
