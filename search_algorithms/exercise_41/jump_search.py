#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from typing import List, Union


class JumpSearch:
    """
    A jump search algorithm is a searching algorithm used to find the position of a specific element within a sorted
    list or array. It combines both linear search and binary search to efficiently locate the target element within
    the collection. It is an improvement on linear search in that it divides the collection into smaller blocks or
    "jumps" and then performs a linear search within each block.

    A jump search algorithm typically has a time complexity of approximately O(√n), making it more efficient than
    linear search for large datasets

    The key steps in a jump search algorithm:
    1. Initialise - Start with the entire sorted list or array
    2. Determine Block Size - Decide on the size of the blocks or "jumps" within the sorted collection. The block
       size/jump size is typically chosen as the square root of the number of elements (i.e. √n)
    3. Comparison - Carry out the following comparison logic:
       - Set up the first block by setting the initial 'left' index as 0 and the 'right' index as √n - 1
       - Compare the 'right' index value to the target element value, if it is greater than the 'right' index value,
       update the 'left' index to be the 'right' index + 1 and increment the right index by √n - 1
       - Repeat this process
    4. Repeat: Repeat the comparison logic in step 3 until the target value is less than the 'right' index (and thus is
       in the sub-list block between the 'left' and 'right' indices)
    5. Linear search: Once you've identified the block that contains the target element, perform a linear search. This
       involves iterating through the elements in the block, checking each element until you either find the target
       element or have determined it doesn't exist in the block
    """
    def __init__(self, numerical_string_list_helper: NumericStringListHelper, stop_watch: StopWatch):
        self._numerical_string_list_helper = numerical_string_list_helper
        self._stop_watch = stop_watch
        self._jump_search_time = None

    def _get_user_input(self) -> int:
        user_input: str = input('Please enter a single digit: ')
        user_input_string_list: List[str] = self._numerical_string_list_helper.get_validated_string_list(
            user_input, ' '
        )

        if len(user_input_string_list) != 1:
            raise ValueError('You must enter a single digit')

        return int(user_input)

    def jump_search_algorithm(self, target_element_value: int, search_list: List[int]) -> Union[int, None]:
        search_list.sort()
        first_iteration = True

        while True:
            if first_iteration:
                first_iteration = False
                self._stop_watch.start()

            mid_element: int = round(len(search_list) / 2)
            mid_element_value: int = search_list[round(len(search_list) / 2)]

            if mid_element_value == target_element_value:
                self._jump_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return mid_element_value
            elif len(search_list) == 1:
                self._jump_search_time = self._stop_watch.stop()
                self._stop_watch.reset()
                return None
            elif target_element_value < mid_element_value:
                search_list: List[int] = search_list[:mid_element]
            elif target_element_value > mid_element_value:
                search_list: List[int] = search_list[-mid_element:]

    def search_for_target(self):
        target_element_value: int = self._get_user_input()
        search_list: list[int] = [integer for integer in range(10001)]

        binary_search_result: Union[int, None] = self.jump_search_algorithm(target_element_value, search_list)

        if binary_search_result is None:
            print(f'Target Element not found in searched list. Search time was {self._binary_search_time} seconds')
        else:
            print(f"Your target value {target_element_value} was found in {self._binary_search_time} seconds")
