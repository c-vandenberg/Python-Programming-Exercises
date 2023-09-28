#!/usr/bin/env python3

from linked_lists import Node, SinglyLinkedList, DoublyLinkedList


def main():
    singly_linked_list: SinglyLinkedList = SinglyLinkedList()
    doubly_linked_list: DoublyLinkedList = DoublyLinkedList()

    for integer in range(0, 10):
        singly_linked_list.append_node(integer)

    for integer in range(0, 10):
        doubly_linked_list.prepend_node(integer)

    zero_node: Node = doubly_linked_list.remove_node_by_value(5)
    two_node: Node = doubly_linked_list.remove_node_by_position(8)

    five_node: Node = doubly_linked_list.forward_search_node_by_value(6)

    print(singly_linked_list)
    print(doubly_linked_list)


if __name__ == '__main__':
    main()
