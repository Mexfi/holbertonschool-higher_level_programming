#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    index = 0
    try:
        while index < x:
            # Attempt to print each element
            print(my_list[index], end='')
            count += 1
            index += 1
    except IndexError:
        # Reached the end of the list
        pass
    print()
    return count
