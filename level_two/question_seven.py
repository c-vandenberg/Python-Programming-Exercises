#!/usr/bin/env python3

from helpers import string_helpers, exception_helpers


class TwoDimensionalArray:

    def __init__(self, string_list_helper: string_helpers.StringListHelper):
        self.string_list_helper = string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of two numbers:')
        user_input_list: list[str] = self.string_list_helper.get_validated_string_list(user_input, ',')

        if len(user_input_list) != 2:
            raise exception_helpers.DataStructureSizeError(2, len(user_input_list))

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


string_list_helper_obj: string_helpers.StringListHelper() = string_helpers.StringListHelper()
two_dimensional_array_obj = TwoDimensionalArray(string_list_helper_obj)

print(two_dimensional_array_obj.calculate_two_dimensional_array())


