#!/usr/bin/env python3

from print_string import PrintString


def main():
    print_string_instance: PrintString = PrintString()
    print_string_instance.get_string()
    print(print_string_instance.string)


if __name__ == '__main__':
    main()
