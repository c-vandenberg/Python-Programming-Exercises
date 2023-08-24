#!/usr/bin/env python3

from helpers import string_helpers
import math


class SquareRootFormula:
    CONSTANT_C = 50

    CONSTANT_H = 30

    def __init__(self, string_list_helper: string_helpers.StringListHelper):
        self.string_list_helper = string_list_helper

    def _get_user_variables(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of numbers:')

        return self.string_list_helper.get_validated_string_list(user_input, ',')

    def calculate_formula(self):
        variable_d_values: list[str] = self._get_user_variables()
        result_list: list[str] = []

        for variable_d in variable_d_values:
            float_result: float = math.sqrt((2 * self.CONSTANT_C * int(variable_d) / self.CONSTANT_H))
            rounded_result: int = round(float_result)
            result_list.append(str(rounded_result))

        return ",".join(result_list)


string_list_helper_obj: string_helpers.StringListHelper() = string_helpers.StringListHelper()
square_root_formula: SquareRootFormula = SquareRootFormula(string_list_helper_obj)
print(square_root_formula.calculate_formula())
