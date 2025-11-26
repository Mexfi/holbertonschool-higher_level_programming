#!/usr/bin/python3
"""
This module defines the MyList class.
"""

class MyList(list):
"""
A class that inherits from list and provides
a method to print the list sorted.
"""

```
def print_sorted(self):
    """
    Prints the list in ascending sorted order.
    Does not modify the original list.
    """
    print(sorted(self))
```
