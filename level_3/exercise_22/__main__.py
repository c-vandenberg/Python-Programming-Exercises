#!/usr/bin/env python3

from helpers.string_helpers import SubstringFrequencyStringListHelper
from collections import Counter
from substring_frequency_calculator import SubstringFrequencyCalculator


def main():
    substring_frequency_string_list_helper: SubstringFrequencyStringListHelper = SubstringFrequencyStringListHelper()
    counter: Counter = Counter()
    substring_frequency_calculator: SubstringFrequencyCalculator = SubstringFrequencyCalculator(
        substring_frequency_string_list_helper,
        counter
    )
    substring_frequency_calculator.calculate_substring_frequency()


if __name__ == '__main__':
    main()
