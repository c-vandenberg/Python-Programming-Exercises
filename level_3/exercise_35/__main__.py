#!/usr/bin/env python3

from list_comprehension import ListComprehension


def main():
    list_comprehension: ListComprehension = ListComprehension()

    print(list_comprehension.divisible_by_seven_one_to_one_thousand())
    print(list_comprehension.numbers_with_three_one_to_one_thousand())
    print(list_comprehension.count_spaces())
    print(list_comprehension.count_consonants())
    print(list_comprehension.tuples_from_list())
    print(list_comprehension.find_common_numbers_between_lists())
    print(list_comprehension.find_numerical_strings())


if __name__ == '__main__':
    main()
