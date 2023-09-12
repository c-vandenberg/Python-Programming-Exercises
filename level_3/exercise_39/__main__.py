#!/usr/bin/env python3

from assert_statement import AssertStatement


def main():
    assert_statement: AssertStatement = AssertStatement()

    assert_statement.assert_not_divide_by_zero()


if __name__ == '__main__':
    main()
