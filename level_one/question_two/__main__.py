#!/usr/bin/env python3

from integer_factorial import IntegerFactorial
from helpers.string_helpers import NumericStringListHelper


def main():
    numeric_string_list_helper: NumericStringListHelper = NumericStringListHelper()
    integer_factorial: IntegerFactorial = IntegerFactorial(numeric_string_list_helper)
    integer_list: list[int] = integer_factorial.get_integer_list()
    factorials: dict[int, int] = integer_factorial.calculate_factorial(integer_list)
    print(factorials)


if __name__ == '__main__':
    main()
