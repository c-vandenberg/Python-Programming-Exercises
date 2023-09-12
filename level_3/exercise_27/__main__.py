#!/usr/bin/env python3

from list_slicing import ListSlicing


def main():
    list_slicing: ListSlicing = ListSlicing(1, 21)
    print(list_slicing.get_first_five_elements())
    print(list_slicing.get_last_five_elements())
    print(list_slicing.get_all_elements_except_first_five())


if __name__ == '__main__':
    main()
