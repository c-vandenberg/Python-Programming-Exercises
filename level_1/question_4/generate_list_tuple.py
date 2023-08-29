#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper


class GenerateListTuple:
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self._numeric_string_list_helper = numeric_string_list_helper

    def generate_list(self, user_string: str) -> list[str]:
        sanitised_user_string: str = self._numeric_string_list_helper.sanitise_string_whitespace(user_string)
        return self._numeric_string_list_helper.get_validated_numeric_string_list(sanitised_user_string, ',')

    def generate_tuple(self, user_string: str) -> tuple[str]:
        sanitised_user_string: str = self._numeric_string_list_helper.sanitise_string_whitespace(user_string)
        return tuple(self._numeric_string_list_helper.get_validated_numeric_string_list(sanitised_user_string, ','))
