#!/usr/bin/env python3

from map_function_lists import MapFunctionLists


def main():
    map_function_lists: MapFunctionLists = MapFunctionLists(1, 11)
    print(map_function_lists.map_squared_values())
    print(map_function_lists.map_list_squared_even_values())


if __name__ == '__main__':
    main()
