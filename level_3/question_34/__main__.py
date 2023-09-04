#!/usr/bin/env python3

from generator_function import DivisibleBySevenNumberGenerator, InfiniteFibonacciSequence


def main():
    divisible_by_seven_number_generator: DivisibleBySevenNumberGenerator = DivisibleBySevenNumberGenerator()
    print(divisible_by_seven_number_generator.calculate())

    infinite_fibonacci_sequence: InfiniteFibonacciSequence = InfiniteFibonacciSequence()
    print(infinite_fibonacci_sequence.calculate())


if __name__ == '__main__':
    main()
