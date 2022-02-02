import string


class Player:
    def __init__(self, name, symbol, score):
        self.name = name
        self.symbol = symbol
        self.score = score

    def increment_score(self):
        self.score += 1

    def input_name(self):
        name = input(f"{self.name} enter your name (max 20 chars):")
        return name

    def validate_name(self, name):
        if (len(name) > 20 or len(name) == 0):
            return False
        for letter in name:
            if letter not in string.ascii_letters:
                return False
        return True

    def update_name(self, name):
        self.name = name

    def get_name(self):
        while True:
            name = self.input_name()
            if self.validate_name(name):
                self.update_name(name)
                break
            print(
                "Your name should only consist of letters A-Z (either case), and be a max of 20 chars, try again"
            )
        print(
            f"Nice to meet you {self.name}, your symbol on the board will be {self.symbol}"
        )
