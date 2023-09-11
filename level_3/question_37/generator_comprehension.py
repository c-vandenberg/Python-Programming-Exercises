#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from typing import Generator, List


class GeneratorComprehension:
    """
    Generator Comprehension is a concise and powerful way to create Generators in Python. Because Generators
    return a 'lazy iterator', they are created using similar iterator syntax as lists, and so we can use similar
    comprehension syntax (we can use the same comprehension syntax for any iterable)

    The general syntax of generator comprehension is:

    (item expression for item in iterable if condition)

    E.g.

    square_number_generator: Generator[int, None, None] = (x ** 2 for x in range(1, 6)) # Output: [1, 4, 9, 16, 25]

    numbers: list[int]  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers_generator: Generator[int, None, None] = (x for x in numbers if x % 2 ==0)

    text: str = 'Hello World'
    vowels_generator: Generator[int, None, None] = (char for char in text if char.lower() in ['aeiou']
    """

    def __init__(self, numerical_string_list_helper: NumericStringListHelper):
        self.numerical_string_list_helper = numerical_string_list_helper

    @staticmethod
    def divisible_by_seven_generator() -> list[int]:
        divisible_by_seven_generator: Generator[int, None, None] = \
            (integer for integer in range(1, 101) if integer % 7 == 0)

        divisible_by_seven_list: list[int] = []

        for generated_number in divisible_by_seven_generator:
            divisible_by_seven_list.append(generated_number)

        return divisible_by_seven_list

    def even_number_generator(self):
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self.numerical_string_list_helper.get_validated_string_list(user_input, ' ')

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        even_number_generator: Generator[int, None, None] = \
            (integer for integer in range(int(user_input)+1) if integer % 2 == 0)

        even_number_list: List[str] = []
        separator = ','

        for generated_number in even_number_generator:
            even_number_list.append(str(generated_number))

        return separator.join(even_number_list)
