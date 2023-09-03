#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from recursion_exercises import NDividedByNPlusOneSummation, NMinusOnePlusOneHundred, FibonacciSequence


def main():
    numeric_string_list_helper: NumericStringListHelper = NumericStringListHelper()


    fibonacci_sequence: FibonacciSequence = FibonacciSequence(numeric_string_list_helper)

    print(fibonacci_sequence.calculate_sequence())


if __name__ == '__main__':
    main()
