#!/usr/bin/env python3

class TupleSlicing:
    def __init__(self, dict_lower_limit: int, dict_upper_limit: int):
        self._dict_lower_limit = dict_lower_limit
        self._dict_upper_limit = dict_upper_limit

    def _generate_squared_tuple(self) -> tuple[int]:
        squared_list: list[int] = []

        for element in range(self.dict_lower_limit, self.dict_upper_limit):
            squared_list.append(element ** 2)

        return tuple(squared_list)

    def _generate_even_tuple(self) -> tuple[int]:
        even_list: list[int] = []

        for element in range (self.dict_lower_limit, self.dict_upper_limit):
            if element % 2 == 0:
                even_list.append(element)

        return tuple(even_list)

    def print_tuples_halves_separate_lines(self):
        squared_tuple: tuple[int] = self._generate_squared_tuple()

        tuple_half_size: int = int(len(squared_tuple) / 2)

        print(squared_tuple[:tuple_half_size])
        print(squared_tuple[tuple_half_size:])

    def get_first_five_elements(self) -> tuple[int]:
        squared_tuple: tuple[int] = self._generate_squared_tuple()

        return squared_tuple[:5]

    def get_last_five_elements(self) -> tuple[int]:
        squared_tuple: tuple[int] = self._generate_squared_tuple()

        return squared_tuple[-5:]

    def get_all_elements_except_first_five(self) -> tuple[int]:
        squared_tuple: tuple[int] = self._generate_squared_tuple()

        return squared_tuple[5:]

    def get_last_element(self) -> tuple[int]:
        squared_tuple: tuple[int] = self._generate_squared_tuple()

        return squared_tuple[-1]

    @property
    def dict_lower_limit(self) -> int:
        return self._dict_lower_limit

    @dict_lower_limit.setter
    def dict_lower_limit(self, new_dict_lower_limit: int) -> None:
        if new_dict_lower_limit != int:
            raise TypeError('New value for lower limit must be of type int')

        self._dict_lower_limit = new_dict_lower_limit

    @property
    def dict_upper_limit(self) -> int:
        return self._dict_upper_limit

    @dict_upper_limit.setter
    def dict_upper_limit(self, new_dict_upper_limit: int) -> None:
        if new_dict_upper_limit != int:
            raise TypeError('New value for upper limit must be of type int')

        self._dict_upper_limit = new_dict_upper_limit
