from question_four import GenerateListTuple


class SquareRootFormula:
    CONSTANT_C = 50

    CONSTANT_H = 30

    def __init__(self, generate_list_tuple: GenerateListTuple):
        self.generate_list_tuple = generate_list_tuple

    def _get_user_variables(self) -> list[str]:
        user_input: str = input('Please enter a comma separated sequence of numbers')
        sanitised_user_string: str = user_input.replace(" ", "")
        self.generate_list_tuple.validate_user_input(sanitised_user_string)

        return sanitised_user_string.split(',')

    def calculate_formula(self):
