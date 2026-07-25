#!/usr/bin/python3
"""Module that defines a singly linked list and its node."""


class Node:
    """Class defining a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): Data stored in the node.
            next_node (Node, optional): Next node reference (default None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data of the node with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node reference with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class defining a singly linked list."""

    def __init__(self):
        """Initialize an empty SinglyLinkedList."""
        self.__head = None

    def __str__(self):
        """Define printable representation of the singly linked list."""
        nodes = []
        curr = self.__head
        while curr is not None:
            nodes.append(str(curr.data))
            curr = curr.next_node
        return "\n".join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the list in increasing sorted order.

        Args:
            value (int): Value of the new Node to insert.
        """
        new_node = Node(value)

        # Case 1: List is empty or new value is smaller than head
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # Case 2: Insert somewhere in the middle or end
        curr = self.__head
        while (curr.next_node is not None and
               curr.next_node.data < value):
            curr = curr.next_node

        new_node.next_node = curr.next_node
        curr.next_node = new_node
