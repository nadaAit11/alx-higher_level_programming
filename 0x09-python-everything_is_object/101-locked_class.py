#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    This class represents a LockedClass with a restricted set of allowed
    instance attributes.

    Attributes:
    __slots__ (str): The only allowed instance attribute, 'first_name'.
    """
    __slots__ = 'first_name'
