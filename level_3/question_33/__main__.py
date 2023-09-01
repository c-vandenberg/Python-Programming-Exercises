#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from recursion_exercises import NDividedByNPlusOneSummation, NMinusOnePlusOneHundred


def main():
    numeric_string_list_helper: NumericStringListHelper = NumericStringListHelper()
    n_divided_by_n_plus_one_summation: NDividedByNPlusOneSummation = NDividedByNPlusOneSummation(
        numeric_string_list_helper
    )
    print(n_divided_by_n_plus_one_summation.calculate())

    n_minus_one_plus_one_hundred: NMinusOnePlusOneHundred = NMinusOnePlusOneHundred(numeric_string_list_helper)
    print(n_minus_one_plus_one_hundred.calculate())


if __name__ == '__main__':
    main()
