#!/usr/bin/env python3

class DataStructureSizeError(Exception):
    def __init__(self, expected_size: int, actual_size: int):
        self.expected_size = expected_size
        self.actual_size = actual_size
        super().__init__(f"Expected size {expected_size}, but got size {actual_size}")


class CycleError(Exception):
    def __init__(self, message: str = "Cycle detected in graph"):
        self.message = message
        super().__init__(self.message)
