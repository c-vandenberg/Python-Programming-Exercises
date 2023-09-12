#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from level_3.question_40.binary_search import BinarySearch
from interpolation_search import InterpolationSearch


def main():
    numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    stop_watch: StopWatch = StopWatch()

    interpolation_search: InterpolationSearch = InterpolationSearch(numeric_string_helper, stop_watch)
    interpolation_search.search_for_target()


if __name__ == '__main__':
    main()
