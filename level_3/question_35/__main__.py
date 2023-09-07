#!/usr/bin/env python3

from iterable_comprehension import ListComprehension, GeneratorComprehension, DictionaryComprehension


def main():
    list_comprehension: ListComprehension = ListComprehension()

    generator_comprehension: GeneratorComprehension = GeneratorComprehension()

    dictionary_comprehension: DictionaryComprehension = DictionaryComprehension()
    print(dictionary_comprehension.change_value_of_key_in_nested_dictionary())


if __name__ == '__main__':
    main()
