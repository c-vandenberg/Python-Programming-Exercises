#!/usr/bin/env python3

from typing import List
from heaps import MinHeapq, MaxHeapq


def main():
    min_heap_list = [integer for integer in range(0, 101)]

    min_heapq: MinHeapq = MinHeapq()
    min_heap: List[int] = min_heapq.heapify_list(min_heap_list)
    min_root_element: int = min_heapq.pop(min_heap)
    min_heapq.push(min_heap, 110)
    min_heapq.push_pop(min_heap, 102)
    min_heapq.replace_root(min_heap, 1)

    max_heap_list = [integer for integer in range(0, 101)]

    max_heapq: MaxHeapq = MaxHeapq()
    max_heap: List[int] = max_heapq.heapify_list(max_heap_list)
    max_root_element: int = max_heapq.pop(max_heap)
    max_heapq.push(max_heap, 110)
    max_heapq.push_pop(max_heap, 102)
    max_heapq.replace_root(max_heap, 150)


if __name__ == '__main__':
    main()
