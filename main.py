from app.TicTacToe import TicTacToe

if __name__ == "__main__":
    game = TicTacToe("board")
    game.player1.get_name()
    game.player2.get_name()
    game.game_loop()
