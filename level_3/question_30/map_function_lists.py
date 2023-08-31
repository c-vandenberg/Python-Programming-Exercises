#!/usr/bin/env python3


class MapFunctionLists:
    """
    The map() function in Python is used to apply a given function to each item in an iterable
    (such as a list, tuple, or string) and return an iterator containing the results.

    The basic idea behind map() is to transform each element in the iterable using the provided function.

    The general syntax is map(function, iterable)

    E.g.
    def square(x):
        return x ** 2

    numbers = [1, 2, 3, 4, 5]
    squared_numbers = map(square, numbers)

    return list(squared_numbers) ## Output: [1, 4, 9, 16, 25]
    """

    def __init__(self, list_lower_limit: int, list_upper_limit: int):
        self._list_lower_limit = list_lower_limit
        self._list_upper_limit = list_upper_limit

    def _generate_simple_list(self):
        simple_list: list[int] = []

        for element in range (self._list_lower_limit, self._list_upper_limit):
            simple_list.append(element)

        return simple_list

    def map_squared_values(self) -> list[int]:
        simple_list: list[int] = self._generate_simple_list()

        return list(map(lambda x: x ** 2, simple_list))

    def map_list_squared_even_values(self) -> list[int]:
        simple_list: list[int] = self._generate_simple_list()

        even_filtered_list: list[int] = list(filter(lambda x: x % 2 == 0, simple_list))
        return list(map(lambda x: x ** 2, even_filtered_list))
