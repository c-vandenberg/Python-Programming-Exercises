#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper


class SquareNumber:
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self._numeric_string_list_helper = numeric_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a single integer or float: ')

        user_input_string_list = self._numeric_string_list_helper.get_validated_numeric_string_list(user_input, ' ')

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single integer or float')

        return user_input_string_list

    def calculate_square(self):
        user_input = self._get_user_input()

        squared_result: float = 0

        for input in user_input:
            squared_result: float = float(input) ** 2

        return round(squared_result, 2)
