class Board:
    def __init__(self):
        self.gameboard = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def setBoard(self, position, player_symbol):
        self.gameboard[position - 1] = player_symbol

    def display_board(self):
        print(f"     |     |     ")
        print(
            f"  {self.gameboard[0]}  |  {self.gameboard[1]}  |  {self.gameboard[2]}  "
        )
        print(f"     |     |     ")
        print(f"-----|-----|-----")
        print(f"     |     |     ")
        print(
            f"  {self.gameboard[3]}  |  {self.gameboard[4]}  |  {self.gameboard[5]}  "
        )
        print(f"     |     |     ")
        print(f"-----|-----|-----")
        print(f"     |     |     ")
        print(
            f"  {self.gameboard[6]}  |  {self.gameboard[7]}  |  {self.gameboard[8]}  "
        )
        print(f"     |     |     ")

    def get_available_spaces(self):
        available_spaces = []
        index = 0
        for space in self.gameboard:
            if space == " ":
                available_spaces.append(index)
            index += 1
        return self.increase_indexes_by_one(available_spaces)

    def increase_indexes_by_one(self, spaces):
        return [space + 1 for space in spaces]

    def check_if_winner(self, symbol):
        if (
            (
                self.gameboard[0] == symbol
                and self.gameboard[1] == symbol
                and self.gameboard[2] == symbol
            )
            or (
                self.gameboard[3] == symbol
                and self.gameboard[4] == symbol
                and self.gameboard[5] == symbol
            )
            or (
                self.gameboard[6] == symbol
                and self.gameboard[7] == symbol
                and self.gameboard[8] == symbol
            )
            or (
                self.gameboard[0] == symbol
                and self.gameboard[3] == symbol
                and self.gameboard[6] == symbol
            )
            or (
                self.gameboard[1] == symbol
                and self.gameboard[4] == symbol
                and self.gameboard[7] == symbol
            )
            or (
                self.gameboard[2] == symbol
                and self.gameboard[5] == symbol
                and self.gameboard[8] == symbol
            )
            or (
                self.gameboard[0] == symbol
                and self.gameboard[4] == symbol
                and self.gameboard[8] == symbol
            )
            or (
                self.gameboard[6] == symbol
                and self.gameboard[4] == symbol
                and self.gameboard[2] == symbol
            )
        ):
            return True
        else:
            return False

    def check_if_draw(self, symbol):
        if (not self.check_if_winner(symbol)) and " " not in self.gameboard:
            return True
        else:
            return False
