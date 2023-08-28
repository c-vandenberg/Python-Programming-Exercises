#!/usr/bin/env python3

from helpers.string_helpers import NameAgeHeightStringListHelper
from sort_name_age_height_tuples import SortNameAgeHeightTuples


def main():
    name_age_height_string_list_helper: NameAgeHeightStringListHelper = NameAgeHeightStringListHelper()
    sort_name_age_height_tuples: SortNameAgeHeightTuples = SortNameAgeHeightTuples(name_age_height_string_list_helper)
    print(sort_name_age_height_tuples.execute())


if __name__ == '__main__':
    main()
