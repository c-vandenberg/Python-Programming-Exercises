#!/usr/bin/env python3

from helpers.string_helpers import PasswordStringListHelper


class PasswordValidator:
    def __init__(self, password_string_list_helper: PasswordStringListHelper):
        self.password_string_list_helper = password_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input('Please enter a sequence of comma separated passwords for validation: ')

        return self.password_string_list_helper.get_validated_password_string_list(
            user_input,
            ','
        )

    def execute(self):
        validated_passwords: list[str] = self._get_user_input()
        separator = ','

        return separator.join(validated_passwords)
