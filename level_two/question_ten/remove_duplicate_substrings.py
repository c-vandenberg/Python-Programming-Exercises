#!/usr/bin/env python3

from helpers.string_helpers import StringListHelper


class RemoveDuplicateSubstrings:
    def __init__(self, string_list_helper: StringListHelper):
        self.string_list_helper = string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter the text you would like to remove duplicate words from: ')

        return self.string_list_helper.get_validated_string_list(user_input, ' ')

    def execute(self) -> list[str]:
        string_list: list[str] = self._get_user_input()
        string_set = set(string_list)
        return list(set(string_list))
