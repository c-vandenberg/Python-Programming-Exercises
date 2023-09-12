#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from typing import List, Union


class TernarySearch:
    """
    A ternary search algorithm is a divide-and-conquer algorithm used to find the position of a specific element within
    a sorted list or array. It is similar in concept to binary search but divides the search space into three parts
    instead of two. Ternary search is typically used on uniformly distributed datasets and can be more efficient than
    binary search in those cases.

    Ternary search has a time complexity of O(log3(n)), which is more efficient than binary search with its time
    complexity of O(log2(n))

    The key steps in a ternary search algorithm:
    1. Initialise - Start with the entire sorted list or array
    2. Define Two Midpoints - Divide the current search space into three equal parts, and take these two midpoints
    3. Comparison - Compare the target element with the elements at midpoint 1 and midpoint 2:
        - If the target matches the element at either midpoint 1 or midpoint 2, you have found the target
        - If the target is less than the element at midpoint 1, you narrow the search range to the left third/less than
        midpoint 1
        - If the target is greater than the element at midpoint 2, you narrow the search range to the right third/greater
        than midpoint 2
        - If the target is between midpoint 1 and midpoint 2, you can narrow the search range to the middle third/between
        midpoint 1 and midpoint 2
    4. Repeat: Repeat steps 2 and 3 until you have found the target element, or it is determined that it is not in the
       sorted list/array
    """
    def __init__(self, numerical_string_list_helper: NumericStringListHelper, stop_watch: StopWatch):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._stop_watch = stop_watch
        self._ternary_search_time = None

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        return int(user_input)

    def _ternary_search_algorithm(self, target_element_value: int, search_list: List[int]) -> Union[int, None]:
        search_list.sort()
        first_iteration = True

        while True:
            if first_iteration:
                first_iteration = False
                self._stop_watch.start()

            elif len(search_list) == 1 and search_list[0] != target_element_value:
                self._ternary_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return None

            midpoint_1_element: int = round(len(search_list) / 3)
            midpoint_1_element_value: int = search_list[midpoint_1_element]

            midpoint_2_element: int = round(len(search_list) * 2/3)
            midpoint_2_element_value: int = search_list[midpoint_2_element]

            if midpoint_1_element_value == target_element_value:
                self._ternary_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return midpoint_1_element_value
            elif midpoint_2_element_value == target_element_value:
                self._ternary_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return midpoint_2_element_value
            elif target_element_value < midpoint_1_element_value:
                search_list: List[int] = search_list[:midpoint_1_element]
            elif target_element_value > midpoint_2_element_value:
                search_list: List[int] = search_list[-midpoint_2_element:]
            elif midpoint_1_element_value < target_element_value < midpoint_2_element_value:
                search_list: List[int] = search_list[midpoint_1_element:midpoint_2_element]

    def search_for_target(self) -> None:
        target_element_value: int = self._get_user_input()
        search_list: list[int] = [integer for integer in range(100000001)]

        ternary_search_result: Union[int, None] = self._ternary_search_algorithm(target_element_value, search_list)

        if ternary_search_result is None:
            print(f'Target Element not found in searched list. Search time was {self._ternary_search_time} seconds')
        else:
            print(f"Your target value {target_element_value} was found in {self._ternary_search_time} seconds")
