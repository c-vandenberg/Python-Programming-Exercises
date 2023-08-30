#!/usr/bin/env python3

from tuple_slicing import TupleSlicing


def main():
    tuple_slicing: TupleSlicing = TupleSlicing(1, 21)
    tuple_slicing.print_tuples_halves_separate_lines()
    print(tuple_slicing.get_first_five_elements())
    print(tuple_slicing.get_last_five_elements())
    print(tuple_slicing.get_all_elements_except_first_five())


if __name__ == '__main__':
    main()
