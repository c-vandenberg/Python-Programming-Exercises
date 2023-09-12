#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from generator_comprehension import GeneratorComprehension


def main():
    numerical_string_list_helper: NumericStringListHelper = NumericStringListHelper()
    generator_comprehension: GeneratorComprehension = GeneratorComprehension(numerical_string_list_helper)

    print(generator_comprehension.even_number_generator())


if __name__ == '__main__':
    main()
