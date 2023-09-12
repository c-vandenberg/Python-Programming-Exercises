#!/usr/bin/env python3

from helpers.string_helpers import AlphabeticStringListHelper
from capitalise_alphabetic_string import CapitaliseAlphabeticString


def main():
    alphabetic_string_list_helper: AlphabeticStringListHelper = AlphabeticStringListHelper()
    capitalise_alphabetic_string: CapitaliseAlphabeticString = CapitaliseAlphabeticString(alphabetic_string_list_helper)
    print(capitalise_alphabetic_string.capitalise_alphabetic_string())


if __name__ == '__main__':
    main()
