#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from square_number import SquareNumber


def main():
    numeric_string_list_helper: NumericStringListHelper = NumericStringListHelper()
    square_number: SquareNumber = SquareNumber(numeric_string_list_helper)
    print(square_number.calculate_square())


if __name__ == '__main__':
    main()
