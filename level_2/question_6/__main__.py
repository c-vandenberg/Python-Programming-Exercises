#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from square_root_formula import SquareRootFormula


def main():
    numeric_string_list_helper_obj: NumericStringListHelper = NumericStringListHelper()
    square_root_formula: SquareRootFormula = SquareRootFormula(numeric_string_list_helper_obj)
    print(square_root_formula.calculate_formula())


if __name__ == '__main__':
    main()
