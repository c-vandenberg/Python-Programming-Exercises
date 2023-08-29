#!/usr/bin/env python3

class DictSquaredKeys:
    @staticmethod
    def _get_dict_squared_keys() -> dict[int, int]:
        dict_squared_keys: dict[int][int] = {}

        for key in range(1, 4):
            dict_squared_keys[key] = [key ** 2]

        return dict_squared_keys

    def execute(self):
        print(self._get_dict_squared_keys())
