#!/usr/bin/env python3

from divisible_by_not_multiple_of import DivisibleByNotMultipleOf


def main():
    divisible_not_multiple_of = DivisibleByNotMultipleOf(7, 5)
    print(divisible_not_multiple_of.list_integers_in_range(2000, 3200))


if __name__ == '__main__':
    main()
