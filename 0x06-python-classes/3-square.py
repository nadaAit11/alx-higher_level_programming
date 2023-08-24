#!/usr/bin/python3
"""
New class Square
"""


class Square:
    """ Defines a Square """
    def __init__(self, size=0):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square (default: 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the square

        Returns:
            int: The area of the square
        """
        return self.__size ** 2
