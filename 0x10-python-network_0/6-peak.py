#!/usr/bin/python3
"""
Finds the peak value in a list of integers using binary search algorithm.
"""
def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if the peak is on the left side
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        # Check if the peak is on the right side
        else:
            low = mid + 1

    # At this point, low and high will be equal, representing the peak
    return list_of_integers[low]
