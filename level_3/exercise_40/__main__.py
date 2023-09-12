#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from binary_search import BinarySearch


def main():
    numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    stop_watch: StopWatch = StopWatch()
    binary_search: BinarySearch = BinarySearch(numeric_string_helper, stop_watch)
    binary_search.search_for_target()


if __name__ == '__main__':
    main()
