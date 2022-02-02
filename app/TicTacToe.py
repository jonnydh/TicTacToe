from app.Player import Player
from app.Board import Board


class TicTacToe:
    def __init__(self):
        self.welcome()
        self.player1 = Player("Player 1", "X", 0)
        self.player2 = Player("Player 2", "O", 0)
        self.board = None
        self.current_player = self.player1

    def welcome(self):
        print(f"Hello and welcome to this Command Line Interface TicTacToe game!")

    def change_player(self):
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def game_loop(self):
        while True:
            self.board = Board()
            self.round_loop()
            self.display_scoreboard()
            if not self.play_again():
                break
            print("A new game shall begin!")
        print("Thanks for playing :-)")

    def round_loop(self):
        while True:
            self.board.display_board()
            spaces = self.board.get_available_spaces()
            self.get_move(spaces)
            if self.check_if_game_over():
                self.board.display_board()
                break
            self.change_player()

    def format_available_spaces(self, spaces):
        output = ""
        index = 0
        for space in spaces:
            if index < len(spaces) - 2:
                output += f"{str(space)}, "
            elif index < len(spaces) - 1:
                output += f"{str(space)} or "
            else:
                output += str(space)
            index += 1
        return f"Choose from the available spaces: {output}"

    def input_move(self, available_spaces):
        move = input(
            f"It's your turn {self.current_player.name}, choose an available space: {self.format_available_spaces(available_spaces)}\n"
        )
        return move

    def validate_input(self, move, available_spaces):
        return True if int(move) in available_spaces else False

    def get_move(self, available_spaces):
        while True:
            try:
                move = int(self.input_move(available_spaces))
                if self.validate_input(move, available_spaces):
                    break
                print(
                    "Invalid input - please make sure you have chosen an available space."
                )
            except:
                print("Invalid input - please make sure you only input integers!")
        self.board.setBoard(move, self.current_player.symbol)

    def check_if_game_over(self):
        return self.check_winner() or self.check_draw()

    def check_winner(self):
        if self.board.check_if_winner(self.current_player.symbol):
            print(f"We have a winner! {self.current_player.name} has won this round!")
            self.current_player.increment_score()
            return True
        else:
            return False

    def check_draw(self):
        if self.board.check_if_draw(self.current_player.symbol):
            print("It's a draw! Nobody won!")
            return True
        else:
            return False

    def play_again(self):
        while True:
            answer = input(
                "Would you like to play again? Enter 'yes' to play again, or 'no' to quit."
            )
            if answer.lower() == "yes" or answer.lower() == "no":
                break
            print("Invalid input\n")
        return True if answer.lower() == "yes" else False

    def display_scoreboard(self):
        player1_whitespace = 25 - len(self.player1.name)
        player2_whitespace = 25 - len(self.player2.name)

        print(f"==============================")
        print(f"|         SCOREBOARD         |")
        print(f"|============================|")
        print(f"|{self.player1.name}:{player1_whitespace * ' '} {self.player1.score}|")
        print(f"|============================|")
        print(f"|{self.player2.name}:{player2_whitespace * ' '} {self.player2.score}|")
        print(f"==============================")
