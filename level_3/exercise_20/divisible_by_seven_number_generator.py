#!/usr/bin/env python3

from typing import Generator


class DivisibleBySevenNumberGenerator:
    @staticmethod
    def _get_user_input() -> int:
        user_input: str = input('Please enter a single integer: ')
        if (user_input.isdigit()) and ('.' not in user_input) and (' ' not in user_input):
            return int(user_input)

        raise ValueError('Please enter a single integer')

    @staticmethod
    def _divisible_by_seven_generator(upper_range: int) -> Generator[int, None, None]:
        for integer in range(0, upper_range):
            if integer % 7 == 0:
                yield integer

    def generate(self):
        user_input: int = self._get_user_input()
        generated_numbers: Generator[int, None, None] = self._divisible_by_seven_generator(user_input)

        for generated_number in generated_numbers:
            print(generated_number)
