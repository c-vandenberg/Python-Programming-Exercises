#!/usr/bin/env python3

import math
from abc import ABC


class Shape(ABC):
    def __init__(self):
        pass

    def calculate_area(self) -> float:
        return 0.00


class Square(Shape):
    def __init__(self, length: float):
        super().__init__()
        self.length = length

    def calculate_area(self) -> float:
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)
