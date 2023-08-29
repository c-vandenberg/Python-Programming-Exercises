#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper


class IntegerFactorial:
    def __init__(self, numerical_string_list_helper: NumericStringListHelper):
        self.numerical_string_list_helper = numerical_string_list_helper

    def get_integer_list(self) -> list[int]:
        user_input: str = input('PLease enter a comma separated numerical string: ')
        sanitised_user_input: str = self.numerical_string_list_helper.sanitise_string_whitespace(user_input)
        validated_user_string_list = self.numerical_string_list_helper.get_validated_string_list(sanitised_user_input, ',')
        integer_list: list[int] = []

        for validated_string in validated_user_string_list:
            integer_list.append(round(int(validated_string)))

        return integer_list

    def _factorial(self, integer: int) -> int:
        if (integer == 0) or (integer == 1):
            return 1

        return integer * self._factorial(integer - 1)

    def calculate_factorial(self, integer_list: list[int]) -> dict[int, int]:
        factorial_list: dict[int, int] = {}
        for number in integer_list:
            factorial_list[number] = self._factorial(number)
        return factorial_list
