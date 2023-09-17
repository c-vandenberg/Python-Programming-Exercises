#!/usr/bin/env python3

from collections import deque
from typing import Iterable


class StringStack:
    def __init__(self, string_stack: deque):
        self._string_stack = string_stack

    """
    Push string items onto top of the stack
    """
    def push_top(self, string_element: str):
        self._string_stack.append(string_element)

    """
    Push string items onto bottom of the stack
    """
    def push_bottom(self, string_element: str):
        self._string_stack.appendleft(string_element)

    """
    Insert element into particular index in stack
    """
    def insert_element(self, index: int, string_element: str):
        self._string_stack.insert(index, string_element)

    """
    Join string iterable on to top of stack
    """
    def join_top(self, string_iterable: Iterable[str]):
        self._string_stack.extend(string_iterable)

    """
    Join string iterable on to bottom of stack
    """
    def join_bottom(self, string_iterable: Iterable[str]):
        self._string_stack.extendleft(string_iterable)

    """
    Remove and return element on top of the stack
    """
    def pop_top(self) -> str:
        return self._string_stack.pop()

    """
    Remove and return element on bottom of the stack
    """
    def pop_bottom(self) -> str:
        return self._string_stack.popleft()

    """
    Remove particular element from stack
    """
    def remove_element(self, string_element: str):
        self._string_stack.remove(string_element)

    """
    Reverse stack order
    """
    def reverse_stack(self):
        self._string_stack.reverse()
