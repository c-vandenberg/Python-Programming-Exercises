#!/usr/bin/env python3

from collections import deque
from stacks import StringStack


def main():
    stack: deque = deque()
    string_stack: StringStack = StringStack(stack)

    string_stack.push_top('Item 1')
    string_stack.push_top('Item 3')
    string_stack.insert_element(1, 'Item 2')
    string_stack.push_bottom('Item 0')

    string_list_top: list[str] = [
        'Item 4',
        'Item 5',
        'Item 6'
    ]

    string_list_bottom: list[str] = [
        'Item -1',
        'Item -2',
        'Item -3'
    ]

    string_stack.join_top(string_list_top)
    string_stack.join_bottom(string_list_bottom)

    item6 = string_stack.pop_top()
    item_minus_3 = string_stack.pop_bottom()

    string_stack.remove_element('Item 1')
    string_stack.reverse_stack()

    item_minus_2 = string_stack.pop_top()


if __name__ == '__main__':
    main()
