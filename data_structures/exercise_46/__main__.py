#!/usr/bin/env python3

from queue import Queue, LifoQueue, PriorityQueue
from queues import StringFifoQueue, StringLifoQueue, StringPriorityQueue


def main():
    fifo_queue: Queue = Queue()
    string_fifo_queue: StringFifoQueue = StringFifoQueue(fifo_queue)

    # Queue initial size and is empty
    fifo_queue_size: int = string_fifo_queue.queue_size()
    fifo_queue_is_empty: bool = string_fifo_queue.is_empty()
    fifo_queue_is_full: bool = string_fifo_queue.is_full()

    # Add items to queue
    string_fifo_queue.enqueue('Item 1')
    string_fifo_queue.enqueue('Item 2')
    string_fifo_queue.enqueue('Item 3')
    string_fifo_queue.enqueue('Item 4')
    string_fifo_queue.enqueue('Item 5')

    # Queue size and is empty
    fifo_queue_size: int = string_fifo_queue.queue_size()
    fifo_queue_is_empty: bool = string_fifo_queue.is_empty()
    fifo_queue_is_full: bool = string_fifo_queue.is_full()

    # Remove items from queue
    item1: str = string_fifo_queue.dequeue()
    item2: str = string_fifo_queue.dequeue()

    # Queue initial size, is empty and is full
    fifo_queue_size: int = string_fifo_queue.queue_size()
    fifo_queue_is_empty: bool = string_fifo_queue.is_empty()
    fifo_queue_is_full: bool = string_fifo_queue.is_full()

    lifo_queue: LifoQueue = LifoQueue()
    string_lifo_queue: StringLifoQueue = StringLifoQueue(lifo_queue)

    # Queue initial size and is empty
    lifo_queue_size: int = string_lifo_queue.queue_size()
    lifo_queue_is_empty: bool = string_lifo_queue.is_empty()
    lifo_queue_is_full: bool = string_lifo_queue.is_full()

    # Add items to queue
    string_lifo_queue.enqueue('Item 1')
    string_lifo_queue.enqueue('Item 2')
    string_lifo_queue.enqueue('Item 3')
    string_lifo_queue.enqueue('Item 4')
    string_lifo_queue.enqueue('Item 5')

    # Queue size and is empty
    lifo_queue_size: int = string_lifo_queue.queue_size()
    lifo_queue_is_empty: bool = string_lifo_queue.is_empty()
    lifo_queue_is_full: bool = string_lifo_queue.is_full()

    # Remove items from queue
    item1: str = string_lifo_queue.dequeue()
    item2: str = string_lifo_queue.dequeue()

    # Queue initial size, is empty and is full
    fifo_queue_size: int = string_lifo_queue.queue_size()
    fifo_queue_is_empty: bool = string_lifo_queue.is_empty()
    fifo_queue_is_full: bool = string_lifo_queue.is_full()

    priority_queue: PriorityQueue = PriorityQueue()
    string_priority_queue: StringPriorityQueue = StringPriorityQueue(priority_queue)

    # Queue initial size and is empty
    priority_queue_size: int = string_priority_queue.queue_size()
    priority_queue_is_empty: bool = string_priority_queue.is_empty()
    priority_queue_is_full: bool = string_priority_queue.is_full()

    # Add items to queue
    string_priority_queue.enqueue((5, 'Item 1'))
    string_priority_queue.enqueue((2, 'Item 2'))
    string_priority_queue.enqueue((1, 'Item 3'))
    string_priority_queue.enqueue((4, 'Item 4'))
    string_priority_queue.enqueue((3, 'Item 5'))

    # Queue size and is empty
    priority_queue_size: int = string_priority_queue.queue_size()
    priority_queue_is_empty: bool = string_priority_queue.is_empty()
    priority_queue_is_full: bool = string_priority_queue.is_full()

    # Remove items from queue
    item1: str = string_priority_queue.dequeue()
    item2: str = string_priority_queue.dequeue()

    # Queue initial size, is empty and is full
    priority_queue_size: int = string_priority_queue.queue_size()
    priority_queue_is_empty: bool = string_priority_queue.is_empty()
    priority_queue_is_full: bool = string_priority_queue.is_full()


if __name__ == '__main__':
    main()
