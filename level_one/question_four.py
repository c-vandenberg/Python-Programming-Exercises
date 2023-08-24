#!/usr/bin/env python3

from helpers import string_helpers


class GenerateListTuple:
    def __init__(self, string_list_helper: string_helpers.StringListHelper):
        self.string_list_helper = string_list_helper

    def generate_list(self, user_string: str) -> list[str]:
        return self.string_list_helper.get_validated_string_list(user_string, ',')

    def generate_tuple(self, user_string: str) -> tuple[str]:
        return tuple(self.string_list_helper.get_validated_string_list(user_string, ','))


user_sequence: str = input('Enter a sequence of comma separated numbers:')

string_list_helper_obj: string_helpers.StringListHelper() = string_helpers.StringListHelper()
generate_list_tuple: GenerateListTuple = GenerateListTuple(string_list_helper_obj)

print(generate_list_tuple.generate_list(user_sequence))
print(generate_list_tuple.generate_tuple(user_sequence))
