#!/usr/bin/env python3

from abc import ABC


class StringListHelper(ABC):
    def get_validated_string_list(self, pre_split_string: str, character_to_split_string: str) -> list[str]:
        self.validate_string(pre_split_string)

        if (character_to_split_string != ' ') and (character_to_split_string not in pre_split_string):
            raise ValueError(f'Input must contain {character_to_split_string}')

        return pre_split_string.split(character_to_split_string)

    @staticmethod
    def validate_string(unvalidated_string: str):
        if type(unvalidated_string) != str:
            raise TypeError('Input must be a string')

    @staticmethod
    def sanitise_string_whitespace(unsanitised_string: str) -> str:
        return unsanitised_string.replace(" ", "")


class NumericStringListHelper(StringListHelper):
    def get_validated_numeric_string_list(self, unvalidated_string: str, character_to_split_string: str) -> list[str]:
        validated_string_list: list[str] = super().get_validated_string_list(
            unvalidated_string,
            character_to_split_string
        )

        for sub_string in validated_string_list:
            if not sub_string.isnumeric():
                raise ValueError('Your string must contain a sequence of numeric strings')

        return validated_string_list


class AlphabeticStringListHelper(StringListHelper):
    def get_validated_alphabetic_string_list(self, unvalidated_string: str, character_to_split_string: str):
        validated_string_list: list[str] = super().get_validated_string_list(
            unvalidated_string,
            character_to_split_string
        )

        for sub_string in validated_string_list:
            if not sub_string.isalpha():
                raise ValueError('Your string must contain a sequence of alphabetic strings')

        return validated_string_list


class BinaryStringListHelper(StringListHelper):
    def get_validated_binary_string_list(self, unvalidated_string: str, character_to_split_string: str):
        validated_string_list: list[str] = super().get_validated_string_list(
            unvalidated_string,
            character_to_split_string
        )

        for sub_string in validated_string_list:
            if not self._is_binary(sub_string):
                raise ValueError('Your string must contain a sequence of binary strings')

        return validated_string_list

    @staticmethod
    def _is_binary(string_sequence: str) -> bool:
        for substring in string_sequence:
            if (substring != '0') and (substring != '1'):
                return False

        return True
