#!/usr/bin/env python3

from generate_list_tuple import GenerateListTuple
from helpers.string_helpers import NumericStringListHelper


def main():
    user_sequence: str = input('Enter a sequence of comma separated numbers: ')

    numeric_string_list_helper_obj: NumericStringListHelper = NumericStringListHelper()
    generate_list_tuple: GenerateListTuple = GenerateListTuple(numeric_string_list_helper_obj)

    print(generate_list_tuple.generate_list(user_sequence))
    print(generate_list_tuple.generate_tuple(user_sequence))


if __name__ == '__main__':
    main()
