#!/usr/bin/env python3

from helpers.string_helpers import AlphabeticStringListHelper


class AlphabetiseStringSequence:
    def __init__(self, alphabetic_string_list_helper: AlphabeticStringListHelper):
        self._alphabetic_string_list_helper = alphabetic_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of alphabetical strings: ')
        sanitised_user_input: str = self._alphabetic_string_list_helper.sanitise_string_whitespace(user_input)
        return self._alphabetic_string_list_helper.get_validated_alphabetic_string_list(
            sanitised_user_input,
            ','
        )

    def alphabetise_user_input(self) -> str:
        separator = ','
        return separator.join(sorted(self._get_user_input()))
