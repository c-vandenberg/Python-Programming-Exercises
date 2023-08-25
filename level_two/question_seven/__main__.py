#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from two_dimensional_array import TwoDimensionalArray


def main():
    numeric_string_list_helper_obj: NumericStringListHelper = NumericStringListHelper()
    two_dimensional_array_obj = TwoDimensionalArray(numeric_string_list_helper_obj)
    print(two_dimensional_array_obj.calculate_two_dimensional_array())


if __name__ == '__main__':
    main()
