#!/usr/bin/env python3

class DictSquaredKeys:
    def __init__(self, lower_limit: int, upper_limit: int):
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit

    def _get_dict_squared_keys(self) -> dict[int, int]:
        dict_squared_keys: dict[int][int] = {}

        for key in range(self._lower_limit, self._upper_limit):
            dict_squared_keys[key] = [key ** 2]

        return dict_squared_keys

    def execute(self):
        print(self._get_dict_squared_keys())

    @property
    def lower_limit(self) -> int:
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, new_lower_limit: int) -> None:
        if new_lower_limit != int:
            raise TypeError('New value for lower limit must be of type int')

        self._lower_limit = new_lower_limit

    @property
    def upper_limit(self) -> int:
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, new_upper_limit: int) -> None:
        if new_upper_limit != int:
            raise TypeError('New value for upper limit must be of type int')

        self._upper_limit = new_upper_limit
