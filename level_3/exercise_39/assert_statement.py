#!/usr/bin/env python3

from typing import List


class AssertStatement:
    """
    In Python, assert statements are used as a debugging aid that tests a condition as an internal self-check in your
    code. When an assert statement is encountered, Python evaluates the accompanying expression, which should return
    either True or False.

    If the expression evaluates to True, the program continues executing without any issues. However, if the expression
    evaluates to False, an AssertionError exception is raised and the program terminates (unless the exception is
    caught and handled).

    The syntax of an 'assert' statement is as follows:

        assert expression, message
    """

    @staticmethod
    def assert_even_list():
        assertion_list: List[int] = [2, 4, 6, 8, 10]

        for element in assertion_list:
            assert element % 2 == 0, 'List contains an odd element value'

    @staticmethod
    def assert_not_divide_by_zero():
        assertion_list: List[int] = [2, 5, 6, 8, 0]

        for element in assertion_list:
            assert element != 0, 'Cannot divide by zero'
            print(str(2 / element))
