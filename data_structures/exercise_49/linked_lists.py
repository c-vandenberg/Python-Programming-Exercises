#!/usr/bin/env python3

from typing import List, Any, Union


class Node:
    def __init__(self, data: Any):
        self._data = data
        self._next = None

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, new_data: Any) -> None:
        self._data = new_data

    @property
    def next(self) -> Union['Node', None]:
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next


class SinglyLinkedList:
    def __init__(self):
        self._head = None

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, new_head: Node) -> None:
        self._head = new_head

    """Append node to end of linked list"""
    def append_node(self, data: Any) -> None:
        # Create new node
        new_node = Node(data)

        # Check if no nodes in linked list
        if not self._head:
            self.head = new_node
            return

        # Initialise current node as head node
        current_node: Node = self.head

        # Traverse linked list until we hit a node with self.next == None (i.e. we have hit the tail node)
        while current_node.next:
            current_node: Node = current_node.next

        # Set pointer of tail node to point to new node
        current_node.next = new_node

    """Prepend node to beginning of linked list"""
    def prepend_node(self, data: Any):
        # Create new node
        new_node: Node = Node(data)

        # Check if no nodes in linked list
        if not self._head:
            self.head = new_node
            return

        # Set new node pointer to reference head of list. Do this first so that we don't orphan the old head node
        new_node.next = self.head

        # Set new node as new head node
        self.head = new_node

    """Remove and return node from linked list by value"""
    def remove_node_by_value(self, node_value: Any) -> Union[Node, None]:
        # If no nodes in linked list, return None
        if not self._head:
            return None

        # Initialise current node as head node and previous node as None
        current_node: Node = self.head
        previous_node: Union[None, Node] = None

        # If value in head node, set head node as next node in linked list and return current node
        if current_node.data == node_value:
            self.head = current_node.next
            current_node.next = None

            return current_node

        # Traverse linked list until we hit node with desired value
        while current_node.data != node_value:
            previous_node = current_node
            current_node = current_node.next

        # Set previous node pointer to node after current node and return current node
        previous_node.next = current_node.next
        current_node.next = None

        return current_node

    """Remove and return node form linked list by position"""
    def remove_node_by_position(self, node_position: int) -> Union[Node, None]:
        if not self._head:
            return None
        current_node: Node = self.head