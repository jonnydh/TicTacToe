import pytest
from app.TicTacToe import TicTacToe


@pytest.fixture
def game():
    print("Setting up class instance for testing purposes...")
    game = TicTacToe("board")
    return game


def test_welcome(game):
    assert (
        game.welcome()
        == "Hello and welcome to this Command Line Interface TicTacToe game!"
    )


def test_change_player(game):
    # Set current player to player 1
    game.current_player = game.player1
    assert game.current_player == game.player1

    # Check game switches from player 1 to player 2
    game.change_player()
    assert game.current_player == game.player2

    # Check game switches from player2 to player1
    game.change_player()
    assert game.current_player == game.player1
