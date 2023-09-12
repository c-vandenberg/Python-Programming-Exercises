#!/usr/bin/env python3

from remove_duplicate_substrings import RemoveDuplicateSubstrings
from helpers.string_helpers import StringListHelper


def main():
    string_list_helper: StringListHelper = StringListHelper()
    remove_duplicate_substrings: RemoveDuplicateSubstrings = RemoveDuplicateSubstrings(string_list_helper)
    print(remove_duplicate_substrings.execute())


if __name__ == '__main__':
    main()
