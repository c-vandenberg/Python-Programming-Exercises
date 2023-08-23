class GenerateListTuple:
    def __init__(self, user_input: str):
        self.user_input = user_input

    def sanitise_user_string(self):
        return self.user_input.replace(" ", "")

    def validate_user_input(self, user_string: str) -> None:
        if type(self.user_input) != str:
            raise TypeError('Input must be a string')

        split_user_input: list[str] = user_string.split(',')

        for input in split_user_input:
            if not input.isnumeric():
                raise TypeError('Your string must contain a sequence of comma separated numbers')

    @staticmethod
    def generate_list(sanitised_user_string: str) -> list[str]:
        return sanitised_user_string.split(',')

    @staticmethod
    def generate_tuple(sanitised_user_string: str) -> tuple[str]:
        return tuple(sanitised_user_string.split(','))


user_sequence: str = input('Enter a sequence of comma separated numbers:')

generate_list_tuple: GenerateListTuple = GenerateListTuple(user_sequence)
sanitised_input: str = generate_list_tuple.sanitise_user_string()
generate_list_tuple.validate_user_input(sanitised_input)

print(generate_list_tuple.generate_list(sanitised_input))
print(generate_list_tuple.generate_tuple(sanitised_input))
