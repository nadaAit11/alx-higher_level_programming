#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they are smaller than 2 elements
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Add the first elements and the second elements of the tuples
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]

    # Return the resulting tuple
    return (sum_first, sum_second)
