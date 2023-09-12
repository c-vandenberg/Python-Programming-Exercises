#!/usr/bin/env python3

from typing import Generator

"""
    A generator is a special kind of function that returns a 'lazy iterator'. A lazy iterator is a special type of
    iterable that generates values on-the-fly as they are needed, rather than precomputing and storing all the values
    in memory.

    A generator therefore allows you to iterate over a large data set without storing it in memory all at once by
    generating the data set values on-the-fly, making generators memory-efficient and suitable for working with
    large datasets ot infinite sequences.

    Generators are defined using functions with one or more 'yield' statements. When a function contains a 'yield'
    statement, it becomes a generator function. When you call a generator function, it returns a Generator object,
    but the functions code is not executed immediately. Instead, it starts executing when you iterate over the
    Generator object.

    E.g. A large file:

    def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
    """


class DivisibleBySevenNumberGenerator:
    @staticmethod
    def _get_user_input() -> int:
        user_input: str = input('Please enter a single integer: ')
        if (user_input.isdigit()) and ('.' not in user_input) and (' ' not in user_input):
            return int(user_input)

        raise ValueError('Please enter a single integer')

    @staticmethod
    def _divisible_by_seven_generator(upper_range: int) -> Generator[int, None, None]:
        for integer in range(0, upper_range):
            if integer % 7 == 0:
                yield integer

    def calculate(self) -> str:
        user_input: int = self._get_user_input()
        divisible_by_seven_list: list[str] = []
        separator = ','

        divisible_by_seven_generator: Generator[int, None, None] = self._divisible_by_seven_generator(user_input)

        for generated_number in divisible_by_seven_generator:
            divisible_by_seven_list.append(str(generated_number))

        return separator.join(divisible_by_seven_list)


class InfiniteFibonacciSequence:
    @staticmethod
    def _get_user_input() -> int:
        user_input: str = input('Please enter a single integer: ')
        if (user_input.isdigit()) and ('.' not in user_input) and (' ' not in user_input):
            return int(user_input)

        raise ValueError('Please enter a single integer')

    """
    The formula 'a, b = b, a + b' below can be more easily understood by breaking it down:
    1. a is initialised as 0 and b is initialised as 1
    2. We have an infinite loop that yields a (0) then carries out the calculation 
    3. a, b = b, a + b means we create the tuple (b, a + b) and unpack it into a and b
    4. Therefore, in the first loop iteration, this becomes a, b = (1, 0 + 1)
    5. Therefore, a = 1 and b = 1 and we yield a again (1)
    6. In the next loop iteration, it becomes a, b = (1, 1 + 1)
    7. Therefore, a = 1 and b = 2 and we yield a again (1)
    8. In the next loop iteration, it becomes a, b = (2, 1 + 2)
    9. Therefore, a = 2 and b = 3 and we yield a again (2)
    10. In the next loop iteration, it becomes a, b = (3, 2 + 3)
    11. Therefore, a = 3 and b = 5 and we yield a again (3)
    12. In the next loop iteration, it becomes a, b = (5, 3 + 5)
    13. Therefore, a = 5 and b = 8 and we yield a again (5)
    
    Therefore, we have an infinite loop that generates a Fibonacci sequence
    """
    @staticmethod
    def _fibonacci_sequence_generator() -> Generator[int, None, None]:
        a: int = 0
        b: int = 1

        while True:
            yield a
            a, b = b, a + b

    """
    Below we use the next() built-in function. The next() function is used to retrieve the next item in an iterable, 
    such as a generator. When you call next() on an iterable, it advances the internal state and returns the next item
    in the sequence. 
    
    The next() function is very useful in infinite sequences because, if we used a for loop to iterate the infinite 
    sequence, our program would go on forever until segmentation fault occurred
    """
    def calculate(self):
        user_input: int = self._get_user_input()
        fibonacci_generator = self._fibonacci_sequence_generator()
        separator: str = ','
        fibonacci_sequence: list[str] = []

        for input in range(0, user_input):
            fibonacci_sequence.append(str(next(fibonacci_generator)))

        return separator.join(fibonacci_sequence)
