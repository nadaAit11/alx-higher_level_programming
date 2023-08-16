#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = set()

    for i in set_1:
        if i not in set_2:
            unique_elements.add(i)
    for i in set_2:
        if i not in set_1:
            unique_elements.add(i)

    return (unique_elements)
