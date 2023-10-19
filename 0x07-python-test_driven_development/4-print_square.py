#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square of '#' characters.

    Args:
        size (int): The size (length) of the square.

    Raises:
        TypeError: If size is not an integer or is a float.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    if size > 0:
        for _ in range(size):
            print("#" * size)
