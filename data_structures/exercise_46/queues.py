#!/usr/bin/env python3

from queue import Queue, LifoQueue, PriorityQueue


class StringFifoQueue(Queue):
    """Append element to back of queue"""
    def enqueue(self, element_string: str):
        self.put(element_string)

    """Remove and return element at front of queue"""
    def dequeue(self) -> str:
        return self.get()

    """Return True if the queue is empty, False otherwise"""
    def is_empty(self) -> bool:
        return self.empty()

    """Return True if the queue is full, False otherwise"""
    def is_full(self) -> bool:
        return self.full()

    """Return the approximate size of the queue"""
    def queue_size(self) -> int:
        return self.qsize()


class StringLifoQueue(LifoQueue):
    """Append element to back of queue"""
    def enqueue(self, element_string: str):
        self.put(element_string)

    """Remove and return element at front of queue"""
    def dequeue(self) -> str:
        return self.get()

    """Return True if the queue is empty, False otherwise"""
    def is_empty(self) -> bool:
        return self.empty()

    """Return True if the queue is full, False otherwise"""
    def is_full(self) -> bool:
        return self.full()

    """Return the approximate size of the queue"""
    def queue_size(self) -> int:
        return self.qsize()


class StringPriorityQueue(PriorityQueue):
    """Append element to back of queue"""
    def enqueue(self, element_string: tuple[int, str]):
        self.put(element_string)

    """Remove and return element at front of queue"""
    def dequeue(self) -> str:
        return self.get()

    """Return True if the queue is empty, False otherwise"""
    def is_empty(self) -> bool:
        return self.empty()

    """Return True if the queue is full, False otherwise"""
    def is_full(self) -> bool:
        return self.full()

    """Return the approximate size of the queue"""
    def queue_size(self) -> int:
        return self.qsize()
