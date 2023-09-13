#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from typing import List, Union


class BinarySearch:
    """
    A binary search algorithm is a common and efficient algorithm used to search for a specific element in a sorted list
    or array. It works by repeatedly dividing the search range in half until the target element is found, or it is
    determined that the element does not exist in the collection.

    Binary search has a time complexity of O(log n), which makes it significantly faster than linear search (O(n)),
    especially for large data sets.

    The key steps in a binary search algorithm:
    1. Initialise: Start with the entire sorted list or array
    2. Midpoint calculation: Calculate the midpoint of the current search range. This can be done by finding the index
       that is halfway between the left and right bounds of the search range
    3. Comparison: Compare the element at the midpoint to the target element you're searching for. If it matches it, you
       have found the target and the search is successful. If it is smaller than the target, discard everything below
       the midpoint. If it is larger than the target, discard everything larger than the midpoint
    4. Repeat: Repeat steps 2 and 3 until you have found the target element, or it is determined that it is not in the
       sorted list/array
    """
    def __init__(self, numerical_string_list_helper: NumericStringListHelper, stop_watch: StopWatch):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._stop_watch = stop_watch
        self._binary_search_time = None

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1 or not user_input.isdigit():
            raise ValueError('You must enter a single integer')

        return int(user_input)

    @staticmethod
    def binary_search_algorithm(target_element_value: [Union[int, float]],
                                search_list: List[Union[int, float]]) -> Union[int, None]:
        search_list.sort()

        while True:
            mid_element: int = round(len(search_list) / 2)
            mid_element_value: int = search_list[round(len(search_list) / 2)]

            if mid_element_value == target_element_value:
                return mid_element_value
            elif len(search_list) == 1:
                return None
            elif target_element_value < mid_element_value:
                search_list: List[int] = search_list[:mid_element]
            elif target_element_value > mid_element_value:
                search_list: List[int] = search_list[-mid_element:]

    def search_for_target(self):
        target_element_value: int = self._get_user_input()
        search_list: list[int] = [integer for integer in range(100000001)]

        self._stop_watch.start()

        binary_search_result: Union[int, None] = self.binary_search_algorithm(target_element_value, search_list)

        self._binary_search_time = self._stop_watch.stop()
        self._stop_watch.reset()

        if binary_search_result is None:
            print(f'Target Element not found in searched list. Search time was {self._binary_search_time} seconds')
        else:
            print(f"Your target value {target_element_value} was found in {self._binary_search_time} seconds")
