#!/usr/bin/env python3

from typing import List, Union, Generator, Dict


class ListComprehension:
    """
    List Comprehension is a concise and powerful way to create lists in Python. It allows you to create new lists by
    applying an expression to each item in an existing iterable (such as a list, tuple, string or range) and optionally
    filtering the items based on a condition.

    The general syntax of list comprehension is:

    [item expression for item in iterable if condition]

    E.g.

    square_numbers: list[int] = [ x ** 2 for x in range(1, 6)] # Output: [1, 4, 9, 16, 25]

    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers: list[int] = [x for x in numbers if x % 2 == 0] # Output: [2, 4, 6, 8, 10]

    text = 'Hello World'
    vowels = char for char in text where char.lower() in 'aeiou'] # Output: ['e', 'o', 'o']
    """

    @staticmethod
    def divisible_by_seven_one_to_one_thousand() -> list[int]:
        return [integer for integer in range(1, 1000) if integer % 7 == 0]

    @staticmethod
    def numbers_with_three_one_to_one_thousand() -> list[int]:
        return [integer for integer in range(1, 1000) if '3' in str(integer)]

    @staticmethod
    def count_spaces() -> int:
        user_input: str = input('Please enter a string: ')

        if type(user_input) != str:
            raise TypeError('Please enter a string')

        spaces: list[str] = [char for char in user_input if str(char) == ' ']

        return len(spaces)

    @staticmethod
    def count_consonants():
        consonant_count_string: str = \
            "Yellow Yaks like yelling and yawning and yesterday they yodled while eating yuky yams"

        return [char for char in consonant_count_string if char.lower() not in 'aeiou ']

    @staticmethod
    def tuples_from_list() -> list[tuple]:
        index_value_list: list[Union[int, str, float, tuple]] = [
            'hi',
            4,
            8.99,
            'apple',
            ('t', 'b', 'n')
        ]

        return [(index, value) for index, value in enumerate(index_value_list)]

    @staticmethod
    def find_common_numbers_between_lists() -> list[int]:
        list_a: list[int] = [1, 2, 3, 4]
        list_b: list[int] = [2, 3, 4, 5]

        return [integer for integer in list_a if integer in list_b]

    @staticmethod
    def find_numerical_strings() -> list[str]:
        mixed_string = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

        return [char for char in mixed_string if char.isnumeric()]

    @staticmethod
    def odd_even_list() -> list[str]:
        return ['even' if integer % 2 == 0 else 'odd' for integer in range(20)]

    @staticmethod
    def matching_numbers_tuple_list() -> list[tuple]:
        list_a: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list_b: list[int] = [2, 7, 1, 12]

        return [(integer, integer) for integer in list_a if integer in list_b]

    @staticmethod
    def find_four_char_or_less_strings():
        test_string: str = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
        test_string_list: list[str] = test_string.split(' ')

        return [substring for substring in test_string_list if len(substring) < 4]

    @staticmethod
    def divisible_by_two_to_nine():
        return [integer for divider in range(2, 10) for integer in range(1, 1001) if integer % divider == 0]


class GeneratorComprehension:
    """
    Generator Comprehension is a concise and powerful way to create Generators in Python. Because Generators
    return a 'lazy iterator', they are created using similar iterator syntax as lists, and so we can use similar
    comprehension syntax (we can use the same comprehension syntax for any iterable)

    The general syntax of generator comprehension is:

    (item expression for item in iterable if condition)

    E.g.

    square_number_generator: Generator[int, None, None] = (x ** 2 for x in range(1, 6)) # Output: [1, 4, 9, 16, 25]

    numbers: list[int]  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers_generator: Generator[int, None, None] = (x for x in numbers if x % 2 ==0)

    text: str = 'Hello World'
    vowels_generator: Generator[int, None, None] = (char for char in text if char.lower() in ['aeiou']
    """

    @staticmethod
    def divisible_by_seven_generator() -> list[int]:
        divisible_by_seven_generator: Generator[int, None, None] = \
            (integer for integer in range(1, 101) if integer % 7 == 0)

        divisible_by_seven_list: list[int] = []

        for generated_number in divisible_by_seven_generator:
            divisible_by_seven_list.append(generated_number)

        return divisible_by_seven_list


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
    def dict_from_two_lists():
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
    def merge_two_dictionaries():
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
    def extract_keys_from_dictionary():
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
    def delete_keys_from_dictionary():
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
    def rename_key_in_dictionary():
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
    def change_value_of_key_in_nested_dictionary():
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
