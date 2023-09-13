#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from ternary_search import TernarySearch


def main():
    numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    stop_watch: StopWatch = StopWatch()

    ternary_search: TernarySearch = TernarySearch(numeric_string_helper, stop_watch)
    ternary_search.search_for_target()


if __name__ == '__main__':
    main()
