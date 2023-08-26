#!/usr/bin/env python3

from helpers.string_helpers import BinaryStringListHelper
from binary_divisible_by_five import BinaryDivisibleByFive


def main():
    binary_string_list_helper: BinaryStringListHelper = BinaryStringListHelper()
    binary_divisible_by_five: BinaryDivisibleByFive = BinaryDivisibleByFive(binary_string_list_helper)
    print(binary_divisible_by_five.execute())


if __name__ == '__main__':
    main()
