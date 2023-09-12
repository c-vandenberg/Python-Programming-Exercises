#!/usr/bin/env python3

from built_in_function_documentation import BuiltInFunctionDocumentation


def main():
    built_in_function_documentation: BuiltInFunctionDocumentation = BuiltInFunctionDocumentation()
    built_in_function_documentation.abs_function_documentation()
    built_in_function_documentation.int_function_documentation()
    built_in_function_documentation.input_documentation()


if __name__ == '__main__':
    main()
