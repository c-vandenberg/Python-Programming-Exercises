#!/usr/bin/env python3

from filter_function_lists import FilterFunctionList


def main():
    filter_function_lists: FilterFunctionList = FilterFunctionList(1, 11)
    print(filter_function_lists.filter_simple_list_even_elements())
    print(filter_function_lists.filter_simple_list_prime_numbers())


if __name__ == '__main__':
    main()
