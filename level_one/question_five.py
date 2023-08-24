#!/usr/bin/env python3

import unittest
from unittest.mock import patch


class SimpleStringClass:
    def __init__(self):
        self._string = ""

    def get_string(self):
        user_string: str = input('Enter a string:')

        if type(user_string) != str:
            raise TypeError('You must enter a string')

        self._string = user_string

    @property
    def string(self) -> str:
        return self._string

    @string.setter
    def string(self, new_string: str) -> None:
        self._string = new_string


class SimpleStringClassUnitTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['Test Input'])
    def test_get_string(self, mock_input):
        test_get_string_instance: SimpleStringClass = SimpleStringClass()
        test_get_string_instance.get_string()
        self.assertEqual(test_get_string_instance.string, 'Test Input')

    def test_string_setter_getter(self):
        test_setter_instance: SimpleStringClass = SimpleStringClass()
        test_setter_instance.string = 'Test String 2'
        self.assertEqual(test_setter_instance.string, 'Test String 2')


simple_string_instance: SimpleStringClass = SimpleStringClass()
simple_string_instance.get_string()
print(simple_string_instance.string)
