#!/usr/bin/env python3

import math


class SquareRootFormula:
    CONSTANT_C = 50

    CONSTANT_H = 30

    def _get_user_variables(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of numbers:')
        sanitised_user_string: str = user_input.replace(" ", "")
        self.validate_user_input(sanitised_user_string)

        return sanitised_user_string.split(',')

    @staticmethod
    def validate_user_input(user_string: str) -> None:
        if type(user_string) != str:
            raise TypeError('Input must be a string')

        split_user_input: list[str] = user_string.split(',')

        for input in split_user_input:
            if not input.isnumeric():
                raise TypeError('Your string must contain a sequence of comma separated numbers')

    def calculate_formula(self):
        variable_d_values: list[str] = self._get_user_variables()
        result_list: list[str] = []

        for variable_d in variable_d_values:
            float_result: float = math.sqrt((2 * self.CONSTANT_C * int(variable_d) / self.CONSTANT_H))
            rounded_result: int = round(float_result)
            result_list.append(str(rounded_result))

        return ",".join(result_list)


square_root_formula: SquareRootFormula = SquareRootFormula()
print(square_root_formula.calculate_formula())
