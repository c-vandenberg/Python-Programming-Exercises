#!/usr/bin/env python3

from helpers import string_helpers


class AlphabetiseStringSequence:
    def __init__(self, alphabetic_string_list_helper: string_helpers.AlphabeticStringListHelper):
        self.alphabetic_string_list_helper = alphabetic_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of alphabetical strings:')
        user_input_list: list[str] = self.alphabetic_string_list_helper.get_validated_alphabetic_string_list(
            user_input,
            ','
        )

        return user_input_list

    def alphabetise_user_input(self) -> str:
        separator = ','
        return separator.join(sorted(self._get_user_input()))


alphabetic_string_list_helper_obj: string_helpers.AlphabeticStringListHelper \
    = string_helpers.AlphabeticStringListHelper()

alphabetise_string_sequence: AlphabetiseStringSequence = AlphabetiseStringSequence(alphabetic_string_list_helper_obj)
print(alphabetise_string_sequence.alphabetise_user_input())
