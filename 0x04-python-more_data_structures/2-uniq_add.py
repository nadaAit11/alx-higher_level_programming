#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = set()

    for item in my_list:
        unique_integers.add(item)

    return sum(unique_integers)
