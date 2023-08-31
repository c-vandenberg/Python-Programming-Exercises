#!/usr/bin/env python3

from sympy import isprime


class FilterFunctionList:
    """
    The filter() function in Python is used to filter out elements from an iterable
    (like a list, tuple, or other sequence) based on a given filtering condition.
    It returns an iterator containing the elements from the original iterable that satisfy the condition.

    The filter() function takes two arguments: a function that defines the filtering condition and an
    iterable that you want to filter. The function provided should return True for the elements you want to keep and
    False for the elements you want to exclude.

    The general syntax is filter(function, iterable)

    E.g.

    def is_even(n):
    return n % 2 == 0

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_numbers = filter(is_even, numbers)
    print(list(filtered_numbers)) # Output: [2, 4, 6, 8, 10]
    """

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