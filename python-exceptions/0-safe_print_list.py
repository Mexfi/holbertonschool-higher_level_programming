#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    index = 0
    try:
        while index < x:
            # Print each element without newline, so elements are on the same line
            print(my_list[index], end='')
            count += 1
            index += 1
    except IndexError:
        # End of list reached
        pass
    print()  # New line after printing elements
    return count
