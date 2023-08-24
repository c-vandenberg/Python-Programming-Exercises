#!/usr/bin/env python3

from helpers import string_helpers


class GenerateListTuple:
    def __init__(self, numeric_string_list_helper: string_helpers.NumericStringListHelper):
        self.numeric_string_list_helper = numeric_string_list_helper

    def generate_list(self, user_string: str) -> list[str]:
        return self.numeric_string_list_helper.get_validated_numeric_string_list(user_string, ',')

    def generate_tuple(self, user_string: str) -> tuple[str]:
        return tuple(self.numeric_string_list_helper.get_validated_numeric_string_list(user_string, ','))


user_sequence: str = input('Enter a sequence of comma separated numbers:')

numeric_string_list_helper_obj: string_helpers.NumericStringListHelper = string_helpers.NumericStringListHelper()
generate_list_tuple: GenerateListTuple = GenerateListTuple(numeric_string_list_helper_obj)

print(generate_list_tuple.generate_list(user_sequence))
print(generate_list_tuple.generate_tuple(user_sequence))
