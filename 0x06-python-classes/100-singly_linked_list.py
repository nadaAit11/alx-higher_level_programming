#!/usr/bin/python3
"""Module containing the Node and SinglyLinkedList class."""


class Node:
    """The node class designed for queue, singly linked list, stack."""

    def __init__(self, data, next_node=None):
        """Initialization of the node.
        Args:
            data (int): The integer value to be stored in the node.
            next_node (Node): The next node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: Integer value stored in the node."""
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Node: The next node."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """The singly linked list class"""

    def __init__(self):
        """Initialization of the singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a node in increasing order of the singly linked list.
        Args:
            value (int): The integer value of the node to be inserted into the
                singly linked list.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next_node and value >= curr_node.next_node.data:
                curr_node = curr_node.next_node
            new_node.next_node = curr_node.next_node
            curr_node.next_node = new_node

    def __str__(self):
        """Returns a string containing the integer values of each node on
        separate lines.
        Returns:
            str: The string of integer values.
        """
        string = ""
        curr_node = self.head
        while curr_node:
            string += str(curr_node.data)
            string += "\n"
            curr_node = curr_node.next_node
        return string.strip()
