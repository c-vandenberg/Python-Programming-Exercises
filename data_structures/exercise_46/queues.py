#!/usr/bin/env python3

from queue import Queue, LifoQueue, PriorityQueue


class StringFifoQueue:
    def __init__(self, string_queue: Queue):
        self._string_queue = string_queue

    """
    Append element to back of queue
    """
    def enqueue(self, element_string: str):
        self._string_queue.put(element_string)

    """
    Remove and return element at front of queue
    """
    def dequeue(self) -> str:
        return self._string_queue.get()

    """
    Return True if the queue is empty, False otherwise
    """
    def is_empty(self) -> bool:
        return self._string_queue.empty()

    """
    Return True if the queue is full, False otherwise
    """
    def is_full(self) -> bool:
        return self._string_queue.full()

    """
    Return the approximate size of the queue
    """
    def queue_size(self) -> int:
        return self._string_queue.qsize()


class StringLifoQueue:
    def __init__(self, string_lifo_queue: LifoQueue):
        self._string_lifo_queue = string_lifo_queue

    """
    Append element to back of queue
    """
    def enqueue(self, element_string: str):
        self._string_lifo_queue.put(element_string)

    """
    Remove and return element at front of queue
    """
    def dequeue(self) -> str:
        return self._string_lifo_queue.get()

    """
        Return True if the queue is empty, False otherwise
    """
    def is_empty(self) -> bool:
        return self._string_lifo_queue.empty()

    """
    Return True if the queue is full, False otherwise
    """
    def is_full(self) -> bool:
        return self._string_lifo_queue.full()

    """
    Return the approximate size of the queue
    """
    def queue_size(self) -> int:
        return self._string_lifo_queue.qsize()


class StringPriorityQueue:
    def __init__(self, string_priority_queue: PriorityQueue):
        self._string_priority_queue = string_priority_queue

    """
    Append element to back of queue
    """
    def enqueue(self, element_string: tuple[int, str]):
        self._string_priority_queue.put(element_string)

    """
    Remove and return element at front of queue
    """
    def dequeue(self) -> str:
        return self._string_priority_queue.get()

    """
        Return True if the queue is empty, False otherwise
    """
    def is_empty(self) -> bool:
        return self._string_priority_queue.empty()

    """
    Return True if the queue is full, False otherwise
    """
    def is_full(self) -> bool:
        return self._string_priority_queue.full()

    """
    Return the approximate size of the queue
    """
    def queue_size(self) -> int:
        return self._string_priority_queue.qsize()
