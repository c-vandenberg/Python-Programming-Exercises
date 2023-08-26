#!/usr/bin/env python3

from helpers.string_helpers import BinaryStringListHelper


class BinaryDivisibleByFive:
    def __init__(self, binary_string_list_helper: BinaryStringListHelper):
        self.binary_string_list_helper = binary_string_list_helper

    def _get_user_input(self):
        user_input = input('Please enter a comma separated sequence of binary strings: ')
        sanitised_user_input: str = self.binary_string_list_helper.sanitise_string_whitespace(user_input)

        return self.binary_string_list_helper.get_validated_binary_string_list(
            sanitised_user_input,
            ','
        )

    @staticmethod
    def _is_divisible_by_five(binary_string: str) -> bool:
        if int(binary_string, 2) % 5 != 0:
            return False

        return True

    def execute(self):
        binary_string_list: list[str] = self._get_user_input()
        divisible_by_five_string_list: list[str] = []
        separator = ','

        for binary_string in binary_string_list:
            if self._is_divisible_by_five(binary_string):
                divisible_by_five_string_list.append(binary_string)

        return separator.join(divisible_by_five_string_list)
