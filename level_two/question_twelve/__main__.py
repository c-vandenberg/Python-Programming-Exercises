#!/usr/bin/env python3

from find_even_numbers import FindEvenNumbers


def main():
    find_even_numbers: FindEvenNumbers = FindEvenNumbers(1000, 3001)
    print(find_even_numbers.get_even_numbers_in_range())


if __name__ == '__main__':
    main()