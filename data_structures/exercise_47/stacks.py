#!/usr/bin/env python3

from collections import deque
from typing import Iterable, Any


class Stack(deque):
    """Push items onto top of the stack"""
    def push_top(self, stack_element: Any):
        self.append(stack_element)

    """Push items onto bottom of the stack"""
    def push_bottom(self, stack_element: Any):
        self.appendleft(stack_element)

    """Insert element into particular index in stack"""
    def insert_element(self, index: int, stack_element: Any):
        self.insert(index, stack_element)

    """Join iterable on to top of stack"""
    def join_top(self, stack_iterable: Iterable[str]):
        self.extend(stack_iterable)

    """Join iterable on to bottom of stack"""
    def join_bottom(self, stack_iterable: Iterable[str]):
        self.extendleft(stack_iterable)

    """Remove and return element on top of the stack"""
    def pop_top(self) -> Any:
        return self.pop()

    """Remove and return element on bottom of the stack"""
    def pop_bottom(self) -> Any:
        return self.popleft()

    """Remove particular element from stack"""
    def remove_element(self, stack_element: Any):
        self.remove(stack_element)

    """Reverse stack order"""
    def reverse_stack(self):
        self.reverse()

    """Clear stack of all elements"""
    def clear_stack(self):
        self.clear()
