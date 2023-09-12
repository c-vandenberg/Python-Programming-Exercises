#!/usr/bin/env python3

class DivisibleByNotMultipleOf:
    def __init__(self, divisible_by: int, not_multiple_of: int):
        self._divisible_by = divisible_by
        self._not_multiple_of = not_multiple_of

    def list_integers_in_range(self, lower_limit: int, upper_limit: int) -> list[int]:
        integer_list: list[int] = []
        for integer in range(lower_limit, upper_limit):
            if (integer % self._divisible_by == 0) and (integer % self._not_multiple_of != 0):
                integer_list.append(integer)
        return integer_list
