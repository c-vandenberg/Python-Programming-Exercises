#!/usr/bin/env python3

from queue import Queue, LifoQueue, PriorityQueue
from typing import Any


class GenericFifoQueue(Queue):
    """Append element to back of queue"""
    def enqueue(self, element: Any):
        self.put(element)

    """Remove and return element at front of queue"""
    def dequeue(self) -> Any:
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


class GenericLifoQueue(LifoQueue):
    """Append element to back of queue"""
    def enqueue(self, element: Any):
        self.put(element)

    """Remove and return element at front of queue"""
    def dequeue(self) -> Any:
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


class GenericPriorityQueue(PriorityQueue):
    """Append element to back of queue"""
    def enqueue(self, element: tuple[int, Any]):
        self.put(element)

    """Remove and return element at front of queue"""
    def dequeue(self) -> Any:
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
