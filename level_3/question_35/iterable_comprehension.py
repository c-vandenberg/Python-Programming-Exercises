#!/usr/bin/env python3

from typing import List, Union


class ListComprehension:
    """
    List Comprehension is a concise and powerful way to create lists in Python. It allows you to create new lists by
    applying an expression to each item in an existing iterable (such as a list, tuple, string or range) and optionally
    filtering the items based on a condition.

    The general syntax of list comprehension is:

    [item expression for item in iterable if condition]

    E.g.

    square_numbers = [ x ** 2 for x in range(1, 6)] # Output: [1, 4, 9, 16, 25]

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [x for x in numbers if x % 2 == 0] # Output: [2, 4, 6, 8, 10]

    text = 'Hello World'
    vowels = char for char in text where char.lower() in 'aeiou'] # Output: ['e', 'o', 'o']
    """

    @staticmethod
    def divisible_by_seven_one_to_one_thousand() -> list[int]:
        return [integer for integer in range(1, 1000) if integer % 7 == 0]

    @staticmethod
    def numbers_with_three_one_to_one_thousand() -> list[int]:
        return [integer for integer in range(1, 1000) if '3' in str(integer)]

    @staticmethod
    def count_spaces() -> int:
        user_input: str = input('Please enter a string: ')

        if type(user_input) != str:
            raise TypeError('Please enter a string')

        spaces: list[str] = [char for char in user_input if str(char) == ' ']

        return len(spaces)

    @staticmethod
    def count_consonants():
        consonant_count_string: str = \
            "Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams"

        return [char for char in consonant_count_string if char.lower() not in 'aeiou ']

    @staticmethod
    def tuples_from_list() -> list[tuple]:
        index_value_list: list[Union[int, str, float, tuple]] = [
            'hi',
            4,
            8.99,
            'apple',
            ('t', 'b', 'n')
        ]

        return [(index, value) for index, value in enumerate(index_value_list)]

    @staticmethod
    def find_common_numbers_between_lists() -> list[int]:
        list_a: list[int] = [1, 2, 3, 4]
        list_b: list[int] = [2, 3, 4, 5]

        return [integer for integer in list_a if integer in list_b]

    @staticmethod
    def find_numerical_strings() -> list[str]:
        mixed_string = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

        return [char for char in mixed_string if char.isnumeric()]

    @staticmethod
    def odd_even_list() -> list[str]:
        return ['even' if integer % 2 == 0 else 'odd' for integer in range(20)]

    @staticmethod
    def matching_numbers_tuple_list():
        list_a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list_b: list[int] = [2, 7, 1, 12]
