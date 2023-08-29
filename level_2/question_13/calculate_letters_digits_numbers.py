#!/usr/bin/env python3

from helpers.string_helpers import StringListHelper


class CalculateLettersDigitsNumbers:
    def __init__(self, string_list_helper: StringListHelper):
        self.string_list_helper = string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter your text: ')

        return self.string_list_helper.get_validated_string_list(
            user_input,
            ' '
        )

    def calculate(self):
        user_input: list[str] = self._get_user_input()
        letter_digit_numbers: dict[str][int] = {'LETTERS': 0, 'DIGITS': 0}

        for substring in user_input:
            for character in substring:
                if character.isalpha():
                    letter_digit_numbers['LETTERS'] += 1
                elif character.isnumeric():
                    letter_digit_numbers['DIGITS'] += 1
                else:
                    continue

        print(f"LETTERS: {letter_digit_numbers['LETTERS']}\nNUMBERS: {letter_digit_numbers['DIGITS']}")
