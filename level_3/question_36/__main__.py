#!/usr/bin/env python3

from dictionary_comprehension import DictionaryComprehension


def main():
    dictionary_comprehension: DictionaryComprehension = DictionaryComprehension()
    print(dictionary_comprehension.square_number_dict() )
    print(dictionary_comprehension.dict_in_range_divided_by_one_hundred())
    print(dictionary_comprehension.new_dict_based_on_old_dict_values())
    print(dictionary_comprehension.dict_from_two_lists())
    print(dictionary_comprehension.merge_two_dictionaries())
    print(dictionary_comprehension.extract_keys_from_dictionary())
    print(dictionary_comprehension.delete_keys_from_dictionary())
    print(dictionary_comprehension.rename_key_in_dictionary())
    print(dictionary_comprehension.change_value_of_key_in_nested_dictionary())


if __name__ == '__main__':
    main()
