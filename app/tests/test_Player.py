import pytest
import io 
from app.Player import Player

def test_always_passes():
    assert True

def test_always_fails():
    assert False

@pytest.fixture
def player():
    print("Setting up class instance for testing purposes...")
    player = Player("Jonny", "X", 0)
    return player

class TestPlayer():
    def test_increment_score(self, player):
        #Score should start at 0
        assert player.score == 0

        player.increment_score()
        assert player.score == 1

        player.increment_score()
        assert player.score == 2

    def test_input_name(self, monkeypatch, player):
        monkeypatch.setattr('sys.stdin', io.StringIO("Josh"))
        name_input = player.input_name()
        assert name_input == "Josh"

    @pytest.mark.parametrize("test_input, expected_result", [
        ("Jonny", True),
        ("Jkjshesfgslkgfjroisg", True),
        ("IGJRGNRGEGRHYJYYT", True),
        ("1", False),
        ("irwjghreigte8", False),
        ("", False),
        (" ", False),
        ("jgrogne fkenerg", False),
        ("-g*&^rgjnrge", False),
        ("jrnegfregkjlmelkgmremgemrge", False)
    ])
    def test_validate_name(self, player, test_input, expected_result):
        assert player.validate_name(test_input) == expected_result

    def test_update_name(self, player):
        assert player.name == "Jonny"
        player.update_name("Millie")
        assert player.name == "Millie"

