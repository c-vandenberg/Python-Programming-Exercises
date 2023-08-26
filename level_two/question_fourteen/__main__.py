#!/usr/bin/env python3

from helpers.string_helpers import StringListHelper
from calculate_upper_lower_case_numbers import CalculateUpperLowerCaseNumbers


def main():
    string_list_helpers: StringListHelper = StringListHelper()
    calculate_upper_lower_case_numbers: CalculateUpperLowerCaseNumbers = CalculateUpperLowerCaseNumbers(string_list_helpers)
    calculate_upper_lower_case_numbers.calculate()


if __name__ == '__main__':
    main()
