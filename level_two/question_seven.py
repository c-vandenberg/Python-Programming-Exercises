#!/usr/bin/env python3

from helpers import string_helpers


class TwoDimensionalArray:

    def __init__(self, string_list_helper: string_helpers.StringListHelper):
        self.string_list_helper = string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of numbers:')
        return self.string_list_helper.get_validated_string_list(user_input, ',')

