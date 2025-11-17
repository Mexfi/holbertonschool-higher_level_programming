#!/usr/bin/python3
def uniq_add(my_list=[]):
    # set() ile benzersiz elemanları al ve sum() ile topla
    return sum(set(my_list))
