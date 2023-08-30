#!/usr/bin/env python3

from sympy import isprime

class FilterFunctionList:
    def __init__(self, list_lower_limit: int, list_upper_limit: int):
        self._list_lower_limit = list_lower_limit
        self._list_upper_limit = list_upper_limit

    def _generate_simple_list(self):
        simple_list: list[int] = []

        for element in range (self._list_lower_limit, self._list_upper_limit):
            simple_list.append(element)

        return simple_list

    def filter_simple_list_even_elements(self) -> list[int]:
        simple_list: list[int] = self._generate_simple_list()

        return list(filter(lambda x: x % 2 == 0, simple_list))

    def filter_simple_list_prime_numbers(self) -> list[int]:
        simple_list: list[int] = self._generate_simple_list()

        return list(filter(lambda x: isprime(x), simple_list))

    @property
    def list_lower_limit(self) -> int:
        return self._list_lower_limit

    @list_lower_limit.setter
    def list_lower_limit(self, new_list_lower_limit: int) -> None:
        if new_list_lower_limit != int:
            raise TypeError('New value for lower limit must be of type int')

        self._list_lower_limit = new_list_lower_limit

    @property
    def list_upper_limit(self) -> int:
        return self._list_upper_limit

    @list_upper_limit.setter
    def list_upper_limit(self, new_list_upper_limit: int) -> None:
        if new_list_upper_limit != int:
            raise TypeError('New value for upper limit must be of type int')

        self._list_upper_limit = new_list_upper_limit