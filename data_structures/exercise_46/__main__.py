#!/usr/bin/env python3

from queues import GenericFifoQueue, GenericLifoQueue, GenericPriorityQueue


def main():
    generic_fifo_queue: GenericFifoQueue = GenericFifoQueue()

    # Queue initial size and is empty
    fifo_queue_size: int = generic_fifo_queue.queue_size()
    fifo_queue_is_empty: bool = generic_fifo_queue.is_empty()
    fifo_queue_is_full: bool = generic_fifo_queue.is_full()

    # Add items to queue
    generic_fifo_queue.enqueue('Item 1')
    generic_fifo_queue.enqueue('Item 2')
    generic_fifo_queue.enqueue('Item 3')
    generic_fifo_queue.enqueue('Item 4')
    generic_fifo_queue.enqueue('Item 5')

    # Queue size and is empty
    fifo_queue_size: int = generic_fifo_queue.queue_size()
    fifo_queue_is_empty: bool = generic_fifo_queue.is_empty()
    fifo_queue_is_full: bool = generic_fifo_queue.is_full()

    # Remove items from queue
    item1: str = generic_fifo_queue.dequeue()
    item2: str = generic_fifo_queue.dequeue()

    # Queue initial size, is empty and is full
    fifo_queue_size: int = generic_fifo_queue.queue_size()
    fifo_queue_is_empty: bool = generic_fifo_queue.is_empty()
    fifo_queue_is_full: bool = generic_fifo_queue.is_full()

    generic_lifo_queue: GenericLifoQueue = GenericLifoQueue()

    # Queue initial size and is empty
    lifo_queue_size: int = generic_lifo_queue.queue_size()
    lifo_queue_is_empty: bool = generic_lifo_queue.is_empty()
    lifo_queue_is_full: bool = generic_lifo_queue.is_full()

    # Add items to queue
    generic_lifo_queue.enqueue('Item 1')
    generic_lifo_queue.enqueue('Item 2')
    generic_lifo_queue.enqueue('Item 3')
    generic_lifo_queue.enqueue('Item 4')
    generic_lifo_queue.enqueue('Item 5')

    # Queue size and is empty
    lifo_queue_size: int = generic_lifo_queue.queue_size()
    lifo_queue_is_empty: bool = generic_lifo_queue.is_empty()
    lifo_queue_is_full: bool = generic_lifo_queue.is_full()

    # Remove items from queue
    item1: str = generic_lifo_queue.dequeue()
    item2: str = generic_lifo_queue.dequeue()

    # Queue initial size, is empty and is full
    fifo_queue_size: int = generic_lifo_queue.queue_size()
    fifo_queue_is_empty: bool = generic_lifo_queue.is_empty()
    fifo_queue_is_full: bool = generic_lifo_queue.is_full()

    generic_priority_queue: GenericPriorityQueue = GenericPriorityQueue()

    # Queue initial size and is empty
    priority_queue_size: int = generic_priority_queue.queue_size()
    priority_queue_is_empty: bool = generic_priority_queue.is_empty()
    priority_queue_is_full: bool = generic_priority_queue.is_full()

    # Add items to queue
    generic_priority_queue.enqueue((5, 'Item 1'))
    generic_priority_queue.enqueue((2, 'Item 2'))
    generic_priority_queue.enqueue((1, 'Item 3'))
    generic_priority_queue.enqueue((4, 'Item 4'))
    generic_priority_queue.enqueue((3, 'Item 5'))

    # Queue size and is empty
    priority_queue_size: int = generic_priority_queue.queue_size()
    priority_queue_is_empty: bool = generic_priority_queue.is_empty()
    priority_queue_is_full: bool = generic_priority_queue.is_full()

    # Remove items from queue
    item1: str = generic_priority_queue.dequeue()
    item2: str = generic_priority_queue.dequeue()

    # Queue initial size, is empty and is full
    priority_queue_size: int = generic_priority_queue.queue_size()
    priority_queue_is_empty: bool = generic_priority_queue.is_empty()
    priority_queue_is_full: bool = generic_priority_queue.is_full()


if __name__ == '__main__':
    main()
