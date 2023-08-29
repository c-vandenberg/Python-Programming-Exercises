#!/usr/bin/env python3

import re
from abc import ABC
from typing import Iterator


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
                raise ValueError('Your string must be numeric')

        return validated_string_list


class AlphabeticStringListHelper(StringListHelper):
    def get_validated_alphabetic_string_list(self, unvalidated_string: str, character_to_split_string: str):
        validated_string_list: list[str] = super().get_validated_string_list(
            unvalidated_string,
            character_to_split_string
        )

        for sub_string in validated_string_list:
            if not sub_string.isalpha():
                raise ValueError('Your string must be alphabetic')

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


class TransactionLogStringListHelper(StringListHelper):
    def get_validated_transaction_log_string_list(self, unvalidated_string: str) -> list[str]:
        self.validate_string(unvalidated_string)
        pattern: str = r'([A-Z]\s\d+)'

        return re.findall(pattern, unvalidated_string)


class PasswordStringListHelper(StringListHelper):
    def get_validated_password_string_list(self, unvalidated_passwords_string: str,
                                           character_to_split_string: str) -> list[str]:

        validated_password_string_list: list[str] = self.get_validated_string_list(
            unvalidated_passwords_string,
            character_to_split_string
        )
        pattern: str = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,12}$'
        accepted_passwords: list[str] = []

        for password in validated_password_string_list:
            if re.match(pattern, password):
                accepted_passwords.append(password)

        return accepted_passwords


class NameAgeHeightStringListHelper(StringListHelper):
    def get_validated_name_age_height_string_list(self, unvalidated_name_age_height_string: str) -> list[str]:
        self.validate_string(unvalidated_name_age_height_string)
        pattern: str = r'[^, ]+(?:,[^, ]+){2}'

        name_age_height_string_list: list[str] = re.findall(pattern, unvalidated_name_age_height_string)

        if len(name_age_height_string_list) < 1:
            raise ValueError("The general format must be 'name, age, height name, age, height")

        return name_age_height_string_list


class RobotMovementStringDictHelper(StringListHelper):
    def get_validated_robot_movement_string_dict(self, unvalidated_robot_movement_string_list: str) -> dict[str: float]:
        sanitised_robot_movement_string: str = self.sanitise_string_whitespace(unvalidated_robot_movement_string_list)
        self.validate_string(sanitised_robot_movement_string)
        validation_pattern: str = r'^(UP|DOWN|LEFT|RIGHT)\d+(,(UP|DOWN|LEFT|RIGHT)\d+)*$'

        if not re.match(validation_pattern, sanitised_robot_movement_string):
            raise ValueError(
                'You must enter a movement string with the general format UP W, DOWN X, LEFT Y, RIGHT Z'
            )

        movement_command_group_pattern: str = r'(?P<direction>UP|DOWN|LEFT|RIGHT)(?P<steps>\d+)'
        movement_commands: dict[str: float] = {}
        movement_matches: Iterator[re.Match[str]] = re.finditer(
            movement_command_group_pattern,
            sanitised_robot_movement_string
        )

        for movement_match in movement_matches:
            movement_commands[movement_match.group('direction')] = float(movement_match.group('steps'))

        return movement_commands


class SubstringFrequencyStringListHelper(StringListHelper):
    def get_validated_substring_frequency_string_list(self, unvalidated_substring_frequency_string: str) -> list[str]:
        self.validate_string(unvalidated_substring_frequency_string)
        substring_split_pattern: str = r'[\s!"#$%&()*+,-./:;<=>?@\[\\\]^_`{|}~]+'

        return re.split(substring_split_pattern, unvalidated_substring_frequency_string)
