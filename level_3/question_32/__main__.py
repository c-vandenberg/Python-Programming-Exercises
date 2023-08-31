#!/usr/bin/env python3

from try_except import TryExcept


def main():
    try_except: TryExcept = TryExcept()
    try_except.divide_by_zero()


if __name__ == '__main__':
    main()
