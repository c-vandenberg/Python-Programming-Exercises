#!/usr/bin/env python3

from linked_lists import Node, SinglyLinkedList, DoublyLinkedList


def main():
    doubly_linked_list: DoublyLinkedList = DoublyLinkedList()

    for integer in range(0, 10):
        doubly_linked_list.append_node(integer)


    test = 'test'


if __name__ == '__main__':
    main()
