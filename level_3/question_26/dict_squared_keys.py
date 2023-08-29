#!/usr/bin/env python3

class DictSquaredKeys:
    def __init__(self, dict_lower_limit: int, dict_upper_limit: int):
        self._dict_lower_limit = dict_lower_limit
        self._dict_upper_limit = dict_upper_limit

    def _get_dict_squared_keys(self) -> dict[int, int]:
        dict_squared_keys: dict[int][int] = {}

        for key in range(self._dict_lower_limit, self._dict_upper_limit):
            dict_squared_keys[key] = [key ** 2]

        return dict_squared_keys

    def execute(self):
        print(self._get_dict_squared_keys())

    @property
    def dict_lower_limit(self) -> int:
        return self._dict_lower_limit

    @dict_lower_limit.setter
    def dict_lower_limit(self, new_dict_lower_limit: int) -> None:
        if new_dict_lower_limit != int:
            raise TypeError('New value for lower limit must be of type int')

        self._dict_lower_limit = new_dict_lower_limit

    @property
    def dict_upper_limit(self) -> int:
        return self._dict_upper_limit

    @dict_upper_limit.setter
    def dict_upper_limit(self, new_dict_upper_limit: int) -> None:
        if new_dict_upper_limit != int:
            raise TypeError('New value for upper limit must be of type int')

        self._dict_upper_limit = new_dict_upper_limit
