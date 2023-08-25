#!/usr/bin/env python3

class OneToNSquareDict:
    square_dict: dict[int, int] = {}

    def calculate(self, integral: int, recursion_depth=0) -> dict[int, int]:
        if recursion_depth == 0:
            self.square_dict: dict[int, int] = {}

        if (integral == 0) or (integral == 1):
            self.square_dict[1] = 1
            return self.square_dict

        self.square_dict[integral] = integral * integral
        return self.calculate(integral - 1, recursion_depth + 1)
