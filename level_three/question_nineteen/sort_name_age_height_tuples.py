#!/usr/bin/env python3

from operator import itemgetter, attrgetter
from helpers.string_helpers import NameAgeHeightStringListHelper


class SortNameAgeHeightTuples:
    def __init__(self, name_age_height_string_list_helper: NameAgeHeightStringListHelper):
        self.name_age_height_string_list_helper = name_age_height_string_list_helper

    def _get_user_input(self) -> list[str]:
        user_input: str = input(
            "Please enter your name, age, height sequence in the general format 'name, age, height name, age, height: "
        )

        return self.name_age_height_string_list_helper.get_validated_name_age_height_string_list(user_input)

    @staticmethod
    def _sort_age(unsorted_name_dict_entry: dict[str]):
        return unsorted_name_dict_entry['age']

    @staticmethod
    def _sort_height(unsorted_name_dict_entry: dict[str]):
        return unsorted_name_dict_entry['height']

    @staticmethod
    def _sort_names(unsorted_name_dict_entry: dict[str]):
        return unsorted_name_dict_entry['name']

    def execute(self) -> tuple[list]:
        validated_name_age_height_string_list = self._get_user_input()

        name_age_height_dict_list: list[dict] = []

        for name_age_height_entry in validated_name_age_height_string_list:
            split_name_age_height_entry: list[str] = name_age_height_entry.split(',')
            dict_entry = {
                'name': split_name_age_height_entry[0],
                'age': split_name_age_height_entry[1],
                'height': split_name_age_height_entry[2]
            }
            name_age_height_dict_list.append(dict_entry)

        height_sorted_name_age_height_dict_list = sorted(name_age_height_dict_list, key=self._sort_age)
        age_sorted_name_age_height_dict_list = sorted(height_sorted_name_age_height_dict_list, key=self._sort_height)
        name_sorted_name_age_height_dict_list = sorted(age_sorted_name_age_height_dict_list, key=self._sort_names)

        sorted_string_list: list[list] = []
        for sorted_entry in name_sorted_name_age_height_dict_list:
            sorted_string_list.append(list(sorted_entry.values()))

        return tuple(sorted_string_list)
