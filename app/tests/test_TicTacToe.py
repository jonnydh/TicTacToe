import pytest
from app.TicTacToe import TicTacToe

def test_always_passes():
    assert True

def test_always_fails():
    assert False

@pytest.fixture()
def game():
    print("Setting up class instance for testing purposes...")
    game = TicTacToe()
    return game

class TestTicTacToe():
    def test_welcome(self, game, capsys):
        game.welcome()
        assert (
            capsys.readouterr().out
            == "Hello and welcome to this Command Line Interface TicTacToe game!\n"
        )

    def test_change_player(self, game):
        # Set current player to player 1
        game.current_player = game.player1
        assert game.current_player == game.player1

        # Check game switches from player 1 to player 2
        game.change_player()
        assert game.current_player == game.player2

        # Check game switches from player2 to player1
        game.change_player()
        assert game.current_player == game.player1

    @pytest.mark.parametrize("test_input, expected", [
        ([7], "Choose from the available spaces: 7"),
        ([4, 6], "Choose from the available spaces: 4 or 6" ),
        ([1,2,3,4,6], "Choose from the available spaces: 1, 2, 3, 4 or 6" ),
        ([1,2,3,4,5,6,7,8,9], "Choose from the available spaces: 1, 2, 3, 4, 5, 6, 7, 8 or 9" )
            ]
        )
    def test_format_available_spaces(self, game, test_input, expected):
        assert game.format_available_spaces(test_input) == expected