class IntegerFactorial:

    def __init__(self, integer_list: list[int]):
        self.integer_list = integer_list

    def _factorial(self, integer: int) -> int:
        if (integer == 0) or (integer == 1):
            return 1

        return integer * self._factorial(integer - 1)

    def calculate_factorial(self) -> dict[int, int]:
        factorial_list: dict[int, int] = {}
        for number in self.integer_list:
            factorial_list[number] = self._factorial(number)
        return factorial_list


factorial_integer_list: list[int] = []
for integer in range(1, 10):
    factorial_integer_list.append(integer)

integer_factorial: IntegerFactorial = IntegerFactorial(factorial_integer_list)
factorials: dict[int, int] = integer_factorial.calculate_factorial()
print(factorials)
