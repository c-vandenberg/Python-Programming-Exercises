#!/usr/bin/env python3

class FindEvenNumbers:
    def __init__(self, lower_limit: int, upper_limit: int):
        self._lower_limit = lower_limit
        self._upper_limit = upper_limit

    def get_even_numbers_in_range(self) -> str:
        even_numbers: list[str] = []
        separator = ','

        for integer in range(self._lower_limit, self._upper_limit):
            integer_string_list: list[str] = list(str(integer))
            is_even: bool = True
            for integer_string in integer_string_list:
                if int(integer_string) % 2 != 0:
                    is_even = False
            if is_even:
                even_numbers.append(str(integer))

        return separator.join(even_numbers)
