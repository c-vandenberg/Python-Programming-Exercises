#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from integer_squared_summation import IntegerSquaredSummation


def main():
    numeric_string_list_helper: NumericStringListHelper = NumericStringListHelper()
    integer_squared_summation: IntegerSquaredSummation = IntegerSquaredSummation(numeric_string_list_helper, 4)
    print(integer_squared_summation.calculate())


if __name__ == '__main__':
    main()
