#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from square_odd_numbers import SquareOddNumbers


def main():
    numeric_string_list_helper: NumericStringListHelper = NumericStringListHelper()
    square_odd_numbers: SquareOddNumbers = SquareOddNumbers(numeric_string_list_helper)
    print(square_odd_numbers.calculate())


if __name__ == '__main__':
    main()
