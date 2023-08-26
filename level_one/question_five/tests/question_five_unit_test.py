#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from level_one.question_five.print_string import PrintString


class SimpleStringClassUnitTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['Test Input'])
    def test_get_string(self, mock_input):
        test_print_string_instance: PrintString = PrintString()
        test_print_string_instance.get_string()
        self.assertEqual(test_print_string_instance.string, 'Test Input')

    def test_string_setter_getter(self):
        test_print_string_instance: PrintString = PrintString()
        test_print_string_instance.string = 'Test String 2'
        self.assertEqual(test_print_string_instance.string, 'Test String 2')