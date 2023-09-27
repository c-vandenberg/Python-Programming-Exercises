#!/usr/bin/env python3

from typing import List, Any, Union


class Node:
    def __init__(self, data: Any):
        self._data = data
        self._next = None
        self._previous = None

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
    def next(self, new_next: 'Node'):
        self._next = new_next

    @property
    def previous(self):
        return self._previous

    @previous.setter
    def previous(self, new_previous: 'Node'):
        self._previous = new_previous


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None

    @property
    def head(self) -> Node:
        return self._head

    @head.setter
    def head(self, new_head: Node) -> None:
        self._head = new_head

    @property
    def tail(self) -> Node:
        return self._tail

    @tail.setter
    def tail(self, new_tail: Node):
        self._tail = new_tail

    """Append node to end of linked list"""
    def append_node(self, data: Any) -> None:
        # Create new node
        new_node: Node = Node(data)

        # If no nodes in linked list, set new node as both head and tail
        if not self.head:
            self.head = new_node
            self.tail = new_node

            return

        # Initialise current node as tail node
        current_node: Node = self.tail

        # Append new node to tail node
        current_node.next = new_node
        new_node.previous = current_node
        self.tail = new_node

    """Prepend node to beginning of linked list"""
    def prepend_node(self, data: Any):
        # Create new node
        new_node: Node = Node(data)

        # Check if no nodes in linked list
        if not self._head:
            self.head = new_node
            self.tail = new_node

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
            # If we have reached the tail node and have not found the node with the given data, raise error
            if not current_node.next:
                raise ValueError(f'Node with value {node_value} not found')

            previous_node = current_node
            current_node = current_node.next

        # Set previous node pointer to node after current node and return current node
        previous_node.next = current_node.next

        # If value was in tail node , set tail node as previous node
        if self.tail == current_node:
            self.tail = previous_node

        current_node.next = None

        return current_node

    """Remove and return node form linked list by position"""
    def remove_node_by_position(self, node_position: int) -> Union[Node, None]:
        # If no nodes in linked list, return None
        if not self._head:
            return None

        # Initialise current node as head node and previous node as None
        current_node: Node = self.head
        previous_node: Union[None, Node] = None

        # If position is 0 (i.e. the head node), set head node as next node in linked list and return current node
        if node_position == 0:
            self.head = current_node.next
            current_node.next = None

            return current_node

        current_position: int = 1

        # Traverse linked list until we hit desired node position
        while current_position != node_position:
            # If we have reached the tail node before hitting the specified node position, raise value error
            if not current_node.next:
                raise ValueError(f'Linked list does not have {node_position} nodes')

            previous_node = current_node
            current_node = current_node.next
            current_position += 1

        # Set previous node pointer to node after current node and return current node
        previous_node.next = current_node.next

        # If value was in tail node , set tail node as previous node
        if self.tail == current_node:
            self.tail = previous_node

        current_node.next = None

        return current_node

    """Search for node in linked list by value"""
    def search_node_by_value(self, node_value: Any) -> Union[Node, None]:
        if not self.head:
            return None

        current_node: Node = self.head

        while current_node.data != node_value:
            current_node = current_node.next

        return current_node


class DoublyLinkedList(LinkedList):
    """Prepend node to beginning of linked list"""
    def prepend_node(self, data: Any) -> None:
        # Create new node
        new_node: Node = Node(data)

        # If no nodes in linked list, set new node as both head and tail
        if not self.head:
            self.head = new_node
            self.tail = new_node

            return

        # Set old head node previous pointer to new node
        old_head_node: Node = self.head
        old_head_node.previous = new_node

        # Set new node next pointer to old head node and set new node as head node
        new_node.next = old_head_node
        self.head = new_node

    """Remove and return node from linked list by value"""
    def remove_node_by_value(self, node_value: Any) -> Union[Node, None]:
        # If no nodes in linked list, return None
        if not self._head:
            return None

        # Initialise current node as head node
        current_node: Node = self.head

        # If value in head node, set head node as next node in linked list, set new head node previous pointer to None,
        # and return current node
        if current_node.data == node_value:
            next_node: Node = current_node.next
            next_node.previous = None
            self.head = next_node
            current_node.next = None

            return current_node

        # Traverse linked list until we hit node with desired value
        while current_node.data != node_value:
            # If we have reached the tail node and have not found the node with the given data, raise error
            if not current_node.next:
                raise ValueError(f'Node with value {node_value} not found')

            current_node = current_node.next

        # Set previous node pointer to node after current node and return current node
        previous_node: Node = current_node.previous
        next_node: Node = current_node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        # If value was in tail node , set tail node as previous node
        if self.tail == current_node:
            self.tail = previous_node

        current_node.next = None

        return current_node

    """Remove and return node form linked list by position"""
    def remove_node_by_position(self, node_position: int) -> Union[Node, None]:
        # If no nodes in linked list, return None
        if not self._head:
            return None

        # Initialise current node as head node
        current_node: Node = self.head

        # If position is 0 (i.e. the head node), set head node as next node in linked list and return current node
        if node_position == 0:
            self.head = current_node.next
            current_node.next = None

            return current_node

        current_position: int = 1

        # Traverse linked list until we hit desired node position
        while current_position != node_position:
            # If we have reached the tail node before hitting the specified node position, raise value error
            if not current_node.next:
                raise ValueError(f'Linked list does not have {node_position} nodes')

            current_node = current_node.next
            current_position += 1

        # Set previous node pointer to node after current node and return current node
        previous_node: Node = current_node.previous
        next_node: Node = current_node.next

        previous_node.next = next_node
        next_node.previous = previous_node

        # If value was in tail node , set tail node as previous node
        if self.tail == current_node:
            self.tail = previous_node

        return current_node
