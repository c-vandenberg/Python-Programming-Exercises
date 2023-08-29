#!/usr/bin/env python3

from helpers.string_helpers import SubstringFrequencyStringListHelper
from collections import Counter


class SubstringFrequencyCalculator:
    def __init__(
            self,
            substring_frequency_string_list_helper: SubstringFrequencyStringListHelper,
            counter: Counter
    ):
        self.substring_frequency_string_list_helper = substring_frequency_string_list_helper
        self.counter = counter

    def _get_user_input(self):
        user_input = input(
            'Please enter a string that you would like to know the word frequency of: '
        )

        return self.substring_frequency_string_list_helper.get_validated_substring_frequency_string_list(user_input)

    def calculate_substring_frequency(self):
        user_input_string_list = self._get_user_input()
        separator: str = '\n'

        for user_input_string in user_input_string_list:
            if not user_input_string.isalpha() and not user_input_string.isnumeric():
                user_input_string_list.remove(user_input_string)

        self.counter.update(user_input_string_list)

        substring_frequency: list[str] = []

        for element, count in self.counter.items():
            substring_frequency.append(f'{element}: {str(count)}')

        substring_frequency.sort()

        print(separator.join(substring_frequency))
