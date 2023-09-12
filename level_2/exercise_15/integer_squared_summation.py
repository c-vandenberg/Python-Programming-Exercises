#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.exception_helpers import DataStructureSizeError
import math


class IntegerSquaredSummation:
    def __init__(self, numeric_string_list_helper: NumericStringListHelper, exponent_range: int):
        self._numeric_string_list_helper = numeric_string_list_helper
        self._exponent_range = exponent_range

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter your single digit: ')
        validated_user_input: list[str] = self._numeric_string_list_helper.get_validated_numeric_string_list(
            user_input,
            ' '
        )

        if len(validated_user_input) != 1:
            raise DataStructureSizeError(1, len(validated_user_input))

        return validated_user_input

    def calculate(self) -> int:
        user_input: list[str] = self._get_user_input()
        result = 0

        for digit in user_input:
            for exponent in range(1, self._exponent_range + 1):
                result += math.pow(int(digit), exponent)

        return result
