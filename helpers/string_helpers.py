#!/usr/bin/env python3


class StringListHelper:

    def get_validated_string_list(self, unvalidated_string: str, character_to_split_string: str) -> list[str]:
        if type(unvalidated_string) != str:
            raise TypeError('Input must be a string')

        if character_to_split_string not in unvalidated_string:
            raise ValueError('Input must be comma separated')

        sanitised_string: str = self._sanitise_string_whitespace(unvalidated_string)
        split_sanitised_string: list[str] = sanitised_string.split(character_to_split_string)

        return split_sanitised_string

    @staticmethod
    def _sanitise_string_whitespace(unsanitised_string: str) -> str:
        return unsanitised_string.replace(" ", "")


class NumericStringListHelper(StringListHelper):
    def get_validated_numeric_string_list(self, unvalidated_string: str, character_to_split_string: str) -> list[str]:
        validated_string_list: list[str] = super().get_validated_string_list(
            unvalidated_string,
            character_to_split_string
        )

        for sub_string in validated_string_list:
            if not sub_string.isnumeric():
                raise TypeError('Your string must contain a sequence of comma separated numbers')

        return validated_string_list

