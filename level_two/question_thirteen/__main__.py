#!/usr/bin/env python3

from helpers.string_helpers import StringListHelper
from calculate_letters_digits_numbers import CalculateLettersDigitsNumbers


def main():
    string_list_helper: StringListHelper = StringListHelper()
    calculate_letters_digits_numbers: CalculateLettersDigitsNumbers = CalculateLettersDigitsNumbers(string_list_helper)
    calculate_letters_digits_numbers.calculate()


if __name__ == '__main__':
    main()
