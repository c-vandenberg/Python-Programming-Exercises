#!/usr/bin/env python3

from typing import Set, Union


class SetComprehension:
    """
    In Python, a set is a data structure of unordered unique elements and are commonly used for tasks that involve
    storing and managing unique values. You can think of sets as similar to lists, with the following main differences:

    1. Uniqueness of Elements - Sets do not allow duplicate elements as each element is unique. Lists on the other hand,
    allow for multiple elements with the same value
    2. Ordering - Sets are unordered, meaning the order in which the elements are added to the set is not preserved.
    Lists are ordered, meaning the order in which the elements are added is preserved
    3. Mutability - Sets are mutable, meaning you can add or remove elements after the set is created. However, the
    elements themselves must contain data types and data structures that are hashable/immutable (i.e. they have a unique
    hash value that doesn't change during their lifetime).
    """

    @staticmethod
    def divisible_by_seven_one_to_one_thousand() -> Set[int]:
        return {integer for integer in range(0, 1001) if integer % 7 == 0}

    @staticmethod
    def matching_numbers_tuple_list() -> Set[tuple]:
        list_a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list_b: list[int] = [2, 7, 1, 12]

        return {(integer, integer) for integer in list_a if integer in list_b}

    @staticmethod
    def tuples_from_list() -> Set[tuple]:
        index_value_list: list[Union[int, str, float, tuple]] = [
            'hi',
            4,
            8.99,
            'apple',
            ('t', 'b', 'n')
        ]

        return {element for element in index_value_list if type(element) == tuple}

    """
    Note that the below code outputs {'even', 'odd'} because sets do not allow duplicate element values
    """
    @staticmethod
    def odd_even_list() -> Set[str]:
        return {'odd' if integer % 2 != 0 else 'even' for integer in range(20)}
