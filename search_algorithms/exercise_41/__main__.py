#!/usr/bin/env python3

from helpers.string_helpers import NumericStringListHelper
from helpers.time_helpers import StopWatch
from jump_search import JumpSearch


def main():
    numeric_string_helper: NumericStringListHelper = NumericStringListHelper()
    stop_watch: StopWatch = StopWatch()

    jump_search: JumpSearch = JumpSearch(numeric_string_helper, stop_watch)
    jump_search.search_for_target()


if __name__ == '__main__':
    main()
