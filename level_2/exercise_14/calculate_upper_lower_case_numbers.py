#!/usr/bin/env python3

from helpers.string_helpers import StringListHelper


class CalculateUpperLowerCaseNumbers:
    def __init__(self, string_list_helper: StringListHelper):
        self._string_list_helper = string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter your text: ')

        return self._string_list_helper.get_validated_string_list(
            user_input,
            ' '
        )

    def calculate(self):
        user_input: list[str] = self._get_user_input()
        upper_lower_case_numbers: dict[str][int] = {'UPPER CASE': 0, 'LOWER CASE': 0}

        for substring in user_input:
            for character in substring:
                if character.isupper():
                    upper_lower_case_numbers['UPPER CASE'] += 1
                elif character.islower():
                    upper_lower_case_numbers['LOWER CASE'] += 1
                else:
                    continue

        print(f"LETTERS: {upper_lower_case_numbers['UPPER CASE']}\nNUMBERS: {upper_lower_case_numbers['LOWER CASE']}")
