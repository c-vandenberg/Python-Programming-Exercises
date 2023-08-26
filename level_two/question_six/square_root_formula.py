#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
import math


class SquareRootFormula:
    CONSTANT_C = 50

    CONSTANT_H = 30

    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def _get_user_variables(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of numbers: ')
        sanitised_user_input: str = self.numeric_string_list_helper.sanitise_string_whitespace(user_input)

        return self.numeric_string_list_helper.get_validated_numeric_string_list(sanitised_user_input, ',')

    def calculate_formula(self):
        variable_d_values: list[str] = self._get_user_variables()
        result_list: list[str] = []

        for variable_d in variable_d_values:
            float_result: float = math.sqrt((2 * self.CONSTANT_C * int(variable_d) / self.CONSTANT_H))
            rounded_result: int = round(float_result)
            result_list.append(str(rounded_result))

        return ",".join(result_list)
