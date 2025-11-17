#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Key'leri alfabetik sıraya göre sırala
    for key in sorted(a_dictionary.keys()):
        # Her key-value çiftini yazdır
        print("{}: {}".format(key, a_dictionary[key]))
