#!/usr/bin/env python3

from helpers.string_helpers import AlphabeticStringListHelper


class CapitaliseAlphabeticString:
    def __init__(self, alphabetic_string_list_helper: AlphabeticStringListHelper):
        self._alphabetic_string_list_helper = alphabetic_string_list_helper

    def _get_user_input(self) -> str:
        user_input: str = input('Please enter a alphabetical string: ')
        self._alphabetic_string_list_helper.validate_string(user_input)

        return user_input

    def capitalise_alphabetic_string(self) -> str:
        user_input: str = self._get_user_input()
        return user_input.upper()
