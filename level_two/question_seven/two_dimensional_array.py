#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.exception_helpers import DataStructureSizeError


class TwoDimensionalArray:
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of two numbers: ')
        sanitised_user_input: str = self.numeric_string_list_helper.sanitise_string_whitespace(user_input)
        user_input_list: list[str] = self.numeric_string_list_helper.get_validated_numeric_string_list(
            sanitised_user_input,
            ','
        )

        if len(user_input_list) != 2:
            raise DataStructureSizeError(2, len(user_input_list))

        return user_input_list

    def calculate_two_dimensional_array(self) -> list[list[int]]:
        user_input_list = self._get_user_input()
        two_dimensional_array: list[list[int]] = []

        outer_list_size: int = round(float(user_input_list[0]))
        inner_list_size: int = round(float(user_input_list[1]))

        for outer_element in range(outer_list_size):
            row: list[int] = []
            for inner_element in range(inner_list_size):
                row.append(outer_element * inner_element)
            two_dimensional_array.append(row)

        return two_dimensional_array
