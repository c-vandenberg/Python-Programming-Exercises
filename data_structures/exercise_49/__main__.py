#!/usr/bin/env python3

from linked_lists import Node, SinglyLinkedList

def main():
    singly_linked_list: SinglyLinkedList = SinglyLinkedList()

    for integer in range(0, 10):
        node: Node = Node(integer)
        singly_linked_list.append_node(node)

    nine_node: Node = singly_linked_list.search_node_by_value(9)


if __name__ == '__main__':
    main()
