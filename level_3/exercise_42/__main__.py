#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from level_3.exercise_40.binary_search import BinarySearch
from exponential_binary_search import ExponentialBinarySearch


def main():
    binary_numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    binary_stop_watch: StopWatch = StopWatch()
    binary_search: BinarySearch = BinarySearch(binary_numeric_string_helper, binary_stop_watch)

    exponential_binary_numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    exponential_binary_stop_watch: StopWatch = StopWatch()
    exponential_binary_search = ExponentialBinarySearch(
        exponential_binary_numeric_string_helper,
        exponential_binary_stop_watch,
        binary_search
    )

    exponential_binary_search.search_for_target()


if __name__ == '__main__':
    main()
