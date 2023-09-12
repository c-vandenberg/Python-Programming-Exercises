#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from typing import List, Union
from level_3.question_40.binary_search import BinarySearch


class ExponentialBinarySearch:
    """
    An exponential binary search algorithm is a searching algorithm used to find a target element within a sorted list
    or array. It is a combination of linear search and binary search techniques and is particularly useful when you
    have a sorted dataset, but you don't know the size of the dataset in advance because it allows you dynamically
    adjust the search range based on the datasets size. It is particularly efficient when your target element is at the
    beginning of the dataset.

    The time complexity of exponential search is O(log n), where n is the size of the dataset.

    The key steps in an exponential search algorithm:
    1. Initialise - Start with the entire sorted list or array
    2. Define Two Indices - start with two indices, 'left' and 'right'. Set 'left' = 0 and 'right' = 1
    3. Comparison - Carry out the following comparison logic:
        If the target matches the element at index 'right', you have found the target
        If the target is greater than the element at index 'right', set index 'left' = (index 'right' - 1) and double
        the value of index 'right' but ensure that it does not exceed the size of the data set. Repeat comparison logic
        If the target is less than the element at index 'right', perform a binary search on the subarray between index
        'left' and index 'right'
    """
    def __init__(
            self,
            numerical_string_list_helper: NumericStringListHelper,
            stop_watch: StopWatch,
            binary_search: BinarySearch
    ):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._stop_watch = stop_watch
        self._binary_search = binary_search
        self._exponential_binary_search_time = None

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        return int(user_input)

    def _exponential_binary_search_algorithm(self, target_element_value: int, search_list: List[int]
                                             ) -> Union[int, None]:
        search_list.sort()
        search_list_size: int = len(search_list)
        left_index: int = 0
        right_index: int = 1
        self._stop_watch.start()

        while right_index <= search_list_size:
            if search_list[right_index] == target_element_value:
                self._exponential_binary_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return search_list[right_index]
            elif target_element_value > search_list[right_index]:
                left_index: int = right_index - 1
                right_index: int = right_index * 2
            elif target_element_value < search_list[right_index]:
                search_sub_list: List[int] = search_list[left_index:right_index]
                exponential_binary_search_result: Union[int, None] = self._binary_search.binary_search_algorithm(
                    target_element_value, search_sub_list
                )
                self._exponential_binary_search_time = self._stop_watch.stop()
                return exponential_binary_search_result

        self._exponential_binary_search_time = self._stop_watch.stop()
        return None

    def search_for_target(self) -> None:
        target_element_value: int = self._get_user_input()
        search_list: list[int] = [integer for integer in range(100000001)]

        exponential_binary_search_result: Union[int, None] = self._exponential_binary_search_algorithm(
            target_element_value,
            search_list
        )

        if exponential_binary_search_result is None:
            print(f'Target Element not found in searched list. Search time was '
                  f'{self._exponential_binary_search_time} seconds')
        else:
            print(
                f"Your target value {target_element_value} was found in {self._exponential_binary_search_time} seconds"
            )
