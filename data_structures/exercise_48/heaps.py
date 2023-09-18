#!/usr/bin/env python3

from typing import List, Any
from abc import ABC, abstractmethod
import heapq


class Heap(ABC):
    """Transform list into a heap, in-place, in O(len(x)) time."""
    @staticmethod
    @abstractmethod
    def heapify_list(heap_list: List[Any]):
        pass

    """Push item onto heap, maintaining the heap structure."""
    @staticmethod
    @abstractmethod
    def push(heap: List[Any], element_value: Any):
        pass

    """Pop the root item off the heap, maintaining the heap structure."""
    @staticmethod
    @abstractmethod
    def pop(heap: List[Any]):
        pass

    """Fast version of a heappush followed by a heappop."""
    @staticmethod
    @abstractmethod
    def push_pop(heap: List[Any], element_value: Any):
        pass

    """Pop and return the current root value, and replace it with the new item."""
    @staticmethod
    @abstractmethod
    def replace_root(heap: List[Any], element_value: Any):
        pass

    """Find the n smallest elements in heap"""
    @staticmethod
    @abstractmethod
    def n_smallest_elements(n: int, heap: List[Any]):
        pass

    """Find the n largest elements in heap"""
    @staticmethod
    @abstractmethod
    def n_largest_elements(n: int, heap: List[Any]):
        pass


class MinHeapq(Heap):
    @staticmethod
    def heapify_list(heap_list: List[Any]):
        heapq.heapify(heap_list)

    @staticmethod
    def push(min_heap: List[Any], element_value: Any):
        heapq.heappush(min_heap, element_value)

    @staticmethod
    def pop(min_heap: List[Any]) -> Any:
        return heapq.heappop(min_heap)

    @staticmethod
    def push_pop(min_heap: List[Any], element_value: Any) -> Any:
        return heapq.heappushpop(min_heap, element_value)

    @staticmethod
    def replace_root(min_heap: List[Any], element_value: Any) -> Any:
        return heapq.heapreplace(min_heap, element_value)

    @staticmethod
    def n_smallest_elements(n: int, min_heap: List[Any]) -> List[Any]:
        return heapq.nsmallest(n, min_heap)

    @staticmethod
    def n_largest_elements(n: int, min_heap: List[Any]) -> List[Any]:
        return heapq.nlargest(n, min_heap)


class MaxHeapq(Heap):
    @staticmethod
    def heapify_list(heap_list: List[Any]) -> List[Any]:
        max_heap: List[Any] = []
        for element in heap_list:
            heapq.heappush(max_heap, -element)

        return max_heap

    @staticmethod
    def push(max_heap: List[Any], element_value: Any):
        heapq.heappush(max_heap, -element_value)

    @staticmethod
    def pop(max_heap: List[Any]) -> Any:
        return -heapq.heappop(max_heap)

    @staticmethod
    def push_pop(max_heap: List[Any], element_value: Any) -> Any:
        return heapq.heappushpop(max_heap, -element_value)

    @staticmethod
    def replace_root(max_heap: List[Any], element_value: Any) -> Any:
        return heapq.heapreplace(max_heap, -element_value)

    @staticmethod
    def n_smallest_elements(n: int, max_heap: List[Any]) -> List[Any]:
        return heapq.nsmallest(n, max_heap)

    @staticmethod
    def n_largest_elements(n: int, max_heap: List[Any]) -> List[Any]:
        return heapq.nlargest(n, max_heap)
