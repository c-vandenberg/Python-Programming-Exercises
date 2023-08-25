#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper


class GenerateListTuple:
    def __init__(self, numeric_string_list_helper: NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def generate_list(self, user_string: str) -> list[str]:
        return self.numeric_string_list_helper.get_validated_numeric_string_list(user_string, ',')

    def generate_tuple(self, user_string: str) -> tuple[str]:
        return tuple(self.numeric_string_list_helper.get_validated_numeric_string_list(user_string, ','))
