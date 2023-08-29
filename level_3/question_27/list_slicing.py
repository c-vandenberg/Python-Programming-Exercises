#!/usr/bin/env python3

class ListSlicing:
    def __init__(self, list_lower_limit: int, list_upper_limit: int):
        self._list_lower_limit = list_lower_limit
        self._list_upper_limit = list_upper_limit

    def _generate_squared_list(self) -> list[int]:
        squared_list: list[int] = []

        for element in range(self._list_lower_limit, self._list_upper_limit):
            squared_list.append(element ** 2)

        return squared_list

    def get_first_five_elements(self) -> list[int]:
        squared_list: list[int] = self._generate_squared_list()

        return squared_list[:5]

    def get_last_five_elements(self) -> list[int]:
        squared_list: list[int] = self._generate_squared_list()

        return squared_list[-5:]

    def get_all_elements_except_first_five(self) -> list[int]:
        squared_list: list[int] = self._generate_squared_list()

        return squared_list[5:]

    @property
    def list_lower_limit(self) -> int:
        return self._list_lower_limit

    @list_lower_limit.setter
    def list_lower_limit(self, new_lower_limit: int) -> None:
        if new_lower_limit != int:
            raise TypeError('New value for lower limit must be of type int')

        self._list_lower_limit = new_lower_limit

    @property
    def list_upper_limit(self) -> int:
        return self._list_upper_limit

    @list_upper_limit.setter
    def list_upper_limit(self, new_upper_limit: int) -> None:
        if new_upper_limit != int:
            raise TypeError('New value for upper limit must be of type int')

        self._list_upper_limit = new_upper_limit
