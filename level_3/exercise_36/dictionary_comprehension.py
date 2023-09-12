#!/usr/bin/env python3

from typing import Dict, Union


class DictionaryComprehension:
    """
    Dictionary Comprehension is a concise and powerful way to create Dictionaries in Python. Like with lists and
    generators, dictionaries are iterable data structures and so can be created using comprehension syntax.

    The general syntax of dictionary comprehension is:

    {key_expression: value_expression for item in iterable if condition}

    E.g.
    square_number_dict: dict[int][int] = {key: x ** 2 for key in range(1, 6)}

    """
    @staticmethod
    def square_number_dict() -> Dict[int, int]:
        return {integer: integer ** 2 for integer in range(1, 6)}

    @staticmethod
    def dict_in_range_divided_by_one_hundred() -> Dict[int, int]:
        return {integer: integer / 100 for integer in range(101)}

    @staticmethod
    def new_dict_based_on_old_dict_values():
        dict_1 = {"NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700}
        return {key: value for key, value in dict_1.items() if value < 2000}

    @staticmethod
    def dict_from_two_lists() -> Dict[int, int]:
        keys = ['Ten', 'Twenty', 'Thirty']
        values = [10, 20, 30]

        """
        The zip() function can be used to pair elements from two iterables together to create a series/list of tuples
        containing a value from each iterable (i.e. element 1 of keys with element 1 of values etc)
        
        Therefore, the below dictionary comprehension syntax iterates over the tuple pairs created by zip() and creates
        key-value pairs in the resulting dictionary
        """
        return {key: value for key, value in zip(keys, values)}

    @staticmethod
    def merge_two_dictionaries() -> Dict[str, int]:
        dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
        dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

        """
        Breaking down the following nested dictionary comprehension:
        
        1. (dict1, dict2) is a tuple containing dict1 and dict2
        2. The comprehension iterates over this tuple, so during the first iteration, 
           dict_iteration is equal to dict1, and during the second iteration, dict_iteration is equal to dict2
        3. For each dict_iteration (which is either dict1 or dict2), the nested comprehension iterates over its
           key-value pairs using 'for key, value in d.items()'
        
        So, the outer loop iterates over the two dictionaries, and the inner loop iterates over the key-value pairs 
        within each dictionary, allowing you to combine key-value pairs from both dictionaries into the merged_dict.
        """

        return {key: value for dict_iteration in (dict1, dict2) for key, value in dict_iteration.items()}

    @staticmethod
    def extract_keys_from_dictionary() -> Dict[str, int]:
        sample_dict = {
            "name": "Kelly",
            "age": 25,
            "salary": 8000,
            "city": "New york"
        }

        # Keys to extract
        keys = ["name", "salary"]

        return {key: value for key, value in sample_dict.items() if key in keys}

    @staticmethod
    def delete_keys_from_dictionary() -> Dict[Union[str, int]]:
        sample_dict = {
            "name": "Kelly",
            "age": 25,
            "salary": 8000,
            "city": "New york"
        }

        # Keys to remove
        keys = ["name", "salary"]

        return {key: value for key, value in sample_dict.items() if key not in keys}

    @staticmethod
    def rename_key_in_dictionary() -> Dict[Union[str, int]]:
        sample_dict = {
            "name": "Kelly",
            "age": 25,
            "salary": 8000,
            "city": "New york"
        }

        """
        In the below code, we use dictionary comprehension to iterate over key-values pairs in 'sample_dict' and use the 
        conditional expression 'location' if key == 'city' else key to determine they key for each pair. If the key is
        'city', it is replaced with 'location', otherwise is remains unchanged
        """
        return {'location' if key == 'city' else key: value for key, value in sample_dict.items()}

    @staticmethod
    def change_value_of_key_in_nested_dictionary() -> Dict[str, Dict]:
        sample_dict = {
            'emp1': {'name': 'John', 'salary': 7500},
            'emp2': {'name': 'Emma', 'salary': 8000},
            'emp3': {'name': 'Brad', 'salary': 500}
        }

        """
        In the below code:
        1. We use dictionary comprehension to iterate over the key-value pairs in 'sample_dict' and check 
        if the key is 'emp3'. 
        2. If it is, we create a new dictionary with the same name and an updated salary of 8500
        3. For all other keys, we keep the original value
        4. The resulting dictionary contains Brad's updated salary, with the salaries of the remaining employees 
           remaining unchanged
        """
        return {key: {'name': value['name'], 'salary': 8500} if key == 'emp3' else value for
                key, value in sample_dict.items()}
