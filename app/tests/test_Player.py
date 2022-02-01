import pytest
from app.Player import Player


@pytest.fixture
def game():
    print("Setting up class instance for testing purposes...")
    player = Player()
    return player
