#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from typing import List, Union
import random


class InterpolationSearch:
    """
    An interpolation search algorithm is a searching algorithm used to find a target element within a sorted list or
    array. The idea behind interpolation searching is to generate a range of discrete probe data points for locations
    to look within the data set.

        Interpolation is a method of finding new data points within the range of an existing data set.

    This is in contrast to binary search, which always goes to the middle element to check.
    Interpolation search on the other hand may go to different probe locations depending on the target element value.
    For example, if the target element value is closer to the value of the last element of the sorted list/array, the
    interpolation search is likely to start the search toward the end of the sorted list/array.

    The basic principle of the formula that generates the data point/probe locations to look in the data set, is to
    return a higher position value when the element to be searched is closer to list[last_index] and a lower position
    value when the element to be searched is closer to list[first_index].

    There are many different formulas used to generate these interpolation probe data points. One example is linear
    interpolation. Linear interpolation takes two data points (the first and last index of the data set), where
    x = element_index and y = list[element_index], and after rearranging y = mx + c to get the following equation:

        probe_position = low_index + (target_element_value - list[low_index])
        * (high_index - low_index)/(list[high_index] - list[low_index])

        where:
            probe_position = the data point location to look

    N.B. If a data set is perfectly uniformly distributed (e.g. range(0, 1000) and the values form an exact straight
         line graph, the above linear interpolation formula should identify the target element value in the first probe
         position calculation if it is present in the data set

    The key steps in an exponential search algorithm:
    1. Initialise - Start with the entire sorted list or array
    2. Define probe_position Data Point - Calculate the value of the probe position to search using interpolation
    equation
    3. Comparison - Carry out the following comparison logic:
        - If the target element value matches the value at list[probe_position], you have found the target
        - If the target element value is greater than the value list[probe_position], calculate the probe position of the
        right sub-list (i.e. list[probe_position + 1] to list[high_index])
        - If the target element value is less than the value at list[probe_position], calculate the probe position of the
        left sub-list (i.e. list[low_index] to list[probe_position - 1])
    4. Repeat - Repeat steps 2 and 3 until you have found the target element, or it is determined that it is not in the
       sorted list/array
    """
    def __init__(
            self,
            numerical_string_list_helper: NumericStringListHelper,
            stop_watch: StopWatch,
    ):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._stop_watch = stop_watch
        self._linear_interpolation_search_time = None

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        return int(user_input)

    def _linear_interpolation_search_algorithm(self, target_element_value: int, search_list: List[int]
                                               ) -> Union[int, None]:
        search_list.sort()
        left_index: int = 0
        right_index: int = len(search_list) - 1
        self._stop_watch.start()

        while left_index <= right_index and search_list[right_index] >= target_element_value >= search_list[left_index]:
            probe_position: int = round(
                (left_index + (target_element_value - search_list[left_index]) *
                 (right_index - left_index) / (search_list[right_index] - search_list[left_index]))
            )

            if search_list[probe_position] == target_element_value:
                self._linear_interpolation_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return search_list[probe_position]
            elif target_element_value < search_list[probe_position]:
                right_index = probe_position - 1
            elif target_element_value > search_list[probe_position]:
                left_index = probe_position + 1

        self._linear_interpolation_search_time = self._stop_watch.stop()
        self._stop_watch.reset()
        return None

    def search_for_target(self) -> None:
        target_element_value: int = self._get_user_input()
        search_list: list[int] = [random.randint(0, 100000) for integer in range(10000)]

        linear_interpolation_search_result: Union[int, None] = self._linear_interpolation_search_algorithm(
            target_element_value,
            search_list
        )

        if linear_interpolation_search_result is None:
            print(f'Target Element not found in searched list. Search time was '
                  f'{self._linear_interpolation_search_time} seconds')
        else:
            print(
                f"Your target value {target_element_value} was found in "
                f"{self._linear_interpolation_search_time} seconds"
            )
