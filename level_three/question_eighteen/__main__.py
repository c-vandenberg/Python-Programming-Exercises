#!/usr/bin/env python3

from helpers.string_helpers import PasswordStringListHelper
from password_valdiator import PasswordValidator


def main():
    password_string_list_helper: PasswordStringListHelper = PasswordStringListHelper()
    password_validator: PasswordValidator = PasswordValidator(password_string_list_helper)
    print(password_validator.execute())


if __name__ == '__main__':
    main()
