#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
import math


class SquareOddNumbers:
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of integers: ')
        return self.numeric_string_list_helper.get_validated_numeric_string_list(
            self.numeric_string_list_helper.sanitise_string_whitespace(user_input),
            ','
        )

    def calculate(self):
        user_input: list[str] = self._get_user_input()
        separator = ','
        result: list[str] = []

        for substring in user_input:
            if int(substring) % 2 != 0:
                result.append(str(round(math.pow(int(substring), 2))))

        return separator.join(result)
