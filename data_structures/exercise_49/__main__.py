#!/usr/bin/env python3

from linked_lists import Node, SinglyLinkedList


def main():
    singly_linked_list: SinglyLinkedList = SinglyLinkedList()

    for integer in range(0, 10):
        singly_linked_list.append_node(integer)

    nine_node: Node = singly_linked_list.search_node_by_value(9)
    four_node: Node = singly_linked_list.remove_node_by_value(4)
    test = 'test'


if __name__ == '__main__':
    main()
