#!/usr/bin/env python3

from helpers.string_helpers import AlphabeticStringListHelper
from alphabetise_string_sequence import AlphabetiseStringSequence


def main():
    alphabetic_string_list_helper_obj: AlphabeticStringListHelper = AlphabeticStringListHelper()
    alphabetise_string_sequence: AlphabetiseStringSequence = AlphabetiseStringSequence(alphabetic_string_list_helper_obj)
    print(alphabetise_string_sequence.alphabetise_user_input())


if __name__ == '__main__':
    main()
