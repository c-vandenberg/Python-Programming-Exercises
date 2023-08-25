#!/usr/bin/env python3


class PrintString:
    def __init__(self):
        self._string = ""

    def get_string(self):
        user_string: str = input('Enter a string: ')

        if type(user_string) != str:
            raise TypeError('You must enter a string')

        self._string = user_string

    @property
    def string(self) -> str:
        return self._string

    @string.setter
    def string(self, new_string: str) -> None:
        self._string = new_string
