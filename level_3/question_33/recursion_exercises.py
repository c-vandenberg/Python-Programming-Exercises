#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper


class IntegerFactorial:
    """
    f(n) = n!
    """
    def __init__(self, numerical_string_list_helper: NumericStringListHelper):
        self._numerical_string_list_helper = numerical_string_list_helper

    def get_integer_list(self) -> list[int]:
        user_input: str = input('PLease enter a comma separated numerical string: ')
        sanitised_user_input: str = self._numerical_string_list_helper.sanitise_string_whitespace(user_input)
        validated_user_string_list = self._numerical_string_list_helper.get_validated_string_list(sanitised_user_input, ',')
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


class NDividedByNPlusOneSummation:
    """
    f(n) = ∑ n/n+1
    """
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def _get_user_input(self) -> list[int]:
        user_input: str = input('Please enter a single integer: ')
        validated_string_list: list[str] = self.numeric_string_list_helper.get_validated_string_list(user_input, ' ')

        if len(validated_string_list) != 1:
            raise ValueError('You must enter a single integer')

        return list(map(lambda x: int(x), validated_string_list))

    def _recursion(self, user_integer: int) -> float:
        if user_integer == 0:
            return 0

        current_recursive_loop_value: float = user_integer / (user_integer + 1)
        return current_recursive_loop_value + self._recursion(user_integer - 1)

    def calculate(self) -> float:
        user_input: list[int] = self._get_user_input()

        for integer in user_input:
            return self._recursion(integer)


class NMinusOnePlusOneHundred:
    """
    f(n) = f(n-1) + 100 where n > 0 and f(0) = 1
    """
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def _get_user_input(self) -> list[int]:
        user_input: str = input('Please enter a single integer greater than zero: ')
        validated_string_list: list[str] = self.numeric_string_list_helper.get_validated_string_list(user_input, ' ')

        if len(validated_string_list) != 1:
            raise ValueError('You must enter a single integer')

        for integer in user_input:
            if int(integer) == 0:
                raise ValueError('You must enter a a non-zero integer')

        return list(map(lambda x: int(x), validated_string_list))

    def _recursion(self, user_integer: int):
        if user_integer == 0:
            return 0

        return self._recursion(user_integer - 1) + 100

    def calculate(self):
        user_input: list[int] = self._get_user_input()

        for input in user_input:
            return self._recursion(input)


class FibonacciSequence:

