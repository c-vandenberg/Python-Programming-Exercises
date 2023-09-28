#!/usr/bin/env python3

from typing import Any, Union


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


class BaseLinkedList:
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
        if not self._head:
            self.head = new_node
            self.tail = new_node

            return

        self._append_node(new_node)

    """Prepend node to beginning of linked list"""
    def prepend_node(self, data: Any):
        # Create new node
        new_node: Node = Node(data)

        # Check if no nodes in linked list
        if not self._head:
            self.head = new_node
            self.tail = new_node

            return

        self._prepend_node(new_node)

    """Remove and return node from linked list by value"""
    def remove_node_by_value(self, node_value: Any) -> Union[Node, None]:
        # If no nodes in linked list, return None
        if not self._head:
            return None

        # If value in head node, remove head node
        if node_value == self.head.data:
            return self._remove_head_node()

        current_node: Node = self.head

        return self._remove_node_by_value(current_node, node_value)

    """Remove and return node form linked list by position"""
    def remove_node_by_position(self, node_position: int) -> Union[Node, None]:
        # If no nodes in linked list, return None
        if not self._head:
            return None

        # If position is 0 (i.e. the head node), remove current head node
        if node_position == 0:
            return self._remove_head_node()

        current_node: Node = self.head

        return self._remove_node_by_position(current_node, node_position)

    """Remove head node and set head.next node as new head node"""
    def _remove_head_node(self) -> Node:
        current_node: Node = self.head
        next_node: Node = current_node.next
        next_node.previous = None
        self.head = next_node
        current_node.next = None

        return current_node

    """Forward search for node in linked list by value"""
    def forward_search_node_by_value(self, node_value: Any) -> Union[Node, None]:
        if not self.head:
            return None

        current_node: Node = self.head

        while current_node.data != node_value:
            # If we have reached the tail node and have not found the node with the given data, raise error
            if not current_node.next:
                raise ValueError(f'Node with value {node_value} not found')

            current_node = current_node.next

        return current_node

    """Print visual representation of linked list data structure"""
    def display_linked_list(self, node_separator: str):
        if not self.head:
            return None

        current_node: Node = self.head
        linked_list_display: str = ""

        while current_node.next:
            linked_list_display += f"{current_node.data} {node_separator} "

            current_node = current_node.next

        linked_list_display += f"{current_node.data}"

        return linked_list_display

    """Append node method logic specific to type of linked list (i.e. singly or doubly linked list)"""
    def _append_node(self, new_node: Node):
        # Logic to be implemented in child class
        pass

    """Prepend node method logic specific to type of linked list (i.e. singly or doubly linked list)"""
    def _prepend_node(self, new_node: Node):
        # Logic to be implemented in child class
        pass

    """Remove node by value logic specific to type of linked list (i.e. singly or doubly linked list)"""
    def _remove_node_by_value(self, current_node: Node, node_value: Any):
        # Logic to be implemented in child class
        pass

    """Remove node by position logic specific to type of linked list (i.e. singly or doubly linked list)"""
    def _remove_node_by_position(self, current_node: Node, node_position: Any):
        # Logic to be implemented in child class
        pass


class SinglyLinkedList(BaseLinkedList):
    def _append_node(self, new_node: Node):
        # Initialise current node as tail node
        current_node: Node = self.tail

        # Append new node to tail node
        current_node.next = new_node
        self.tail = new_node

    def _prepend_node(self, new_node: Node):
        # Set new node pointer to reference head of list. Do this first so that we don't orphan the old head node
        new_node.next = self.head

        # Set new node as new head node
        self.head = new_node

    def _remove_node_by_value(self, current_node: Node, node_value: Any) -> Union[Node, None]:
        # Initialise previous node as None
        previous_node: Union[None, Node] = None

        # Traverse linked list until we hit node with desired value
        while current_node.data != node_value:
            # If we have reached the tail node and have not found the node with the given data, raise error
            if not current_node.next:
                raise ValueError(f'Node with value {node_value} not found')

            previous_node = current_node
            current_node = current_node.next

        # If value was in tail node, set tail node as previous node
        if current_node == self.tail:
            previous_node.next = None
            self.tail = previous_node
        else:
            # Set previous node pointer to node after current node and return current node
            previous_node.next = current_node.next

        current_node.next = None

        return current_node

    def _remove_node_by_position(self, current_node: Node, node_position: int) -> Union[Node, None]:
        # Initialise previous node as None, and initialise current position as zero
        previous_node: Union[None, Node] = None
        current_position: int = 0

        # Traverse linked list until we hit desired node position
        while current_position != node_position:
            # If we have reached the tail node before hitting the specified node position, raise value error
            if not current_node.next:
                raise ValueError(f'Linked list does not have {node_position} nodes')

            previous_node = current_node
            current_node = current_node.next
            current_position += 1

            # If value was in tail node, set tail node as previous node
            if current_node == self.tail:
                previous_node.next = None
                self.tail = previous_node
            else:
                # Set previous node pointer to node after current node and return current node
                previous_node.next = current_node.next

            current_node.next = None

            return current_node


class DoublyLinkedList(BaseLinkedList):
    def _append_node(self, new_node: Node):
        # Initialise current node as tail node
        current_node: Node = self.tail

        # Append new node to tail node
        current_node.next = new_node
        new_node.previous = current_node
        self.tail = new_node

    def _prepend_node(self, new_node: Node):
        # Set new node pointer to reference head of list. Do this first so that we don't orphan the old head node
        new_node.next = self.head
        self.head.previous = new_node

        # Set new node as new head node
        self.head = new_node

    def _remove_node_by_value(self, current_node: Node, node_value: Any) -> Union[Node, None]:
        # Traverse linked list until we hit node with desired value
        while current_node.data != node_value:
            # If we have reached the tail node and have not found the node with the given data, raise error
            if not current_node.next:
                raise ValueError(f'Node with value {node_value} not found')

            current_node = current_node.next

        # Set previous node pointer to node after current node and return current node
        previous_node: Node = current_node.previous

        # If value was in tail node , set tail node as previous node
        if self.tail == current_node:
            previous_node.next = None
            self.tail = previous_node
        else:
            next_node: Node = current_node.next
            previous_node.next = next_node
            next_node.previous = previous_node

        current_node.next = None

        return current_node

    def _remove_node_by_position(self, current_node: Node, node_position: int) -> Union[Node, None]:
        # Initialise current position as zero
        current_position: int = 0

        # Traverse linked list until we hit desired node position
        while current_position != node_position:
            # If we have reached the tail node before hitting the specified node position, raise value error
            if not current_node.next:
                raise ValueError(f'Linked list does not have {node_position} nodes')

            current_node = current_node.next
            current_position += 1

        # Set previous node pointer to node after current node and return current node
        previous_node: Node = current_node.previous

        # If value was in tail node , set tail node as previous node
        if self.tail == current_node:
            previous_node.next = None
            self.tail = previous_node
        else:
            next_node: Node = current_node.next
            previous_node.next = next_node
            next_node.previous = previous_node

        current_node.next = None

        return current_node

    """Backward search for node in linked list by value"""
    def backward_search_node_by_value(self, node_value: Any) -> Union[Node, None]:
        if not self.head:
            return None

        current_node: Node = self.tail

        while current_node.data != node_value:
            # If we have reached the head node and have not found the node with the given data, raise error
            if not current_node.previous:
                raise ValueError(f'Node with value {node_value} not found')

            current_node = current_node.previous

        return current_node
