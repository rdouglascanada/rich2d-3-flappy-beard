from pygame import Rect
from player_character import PlayerCharacter

class GameManager:
    def __init__(self, window_width=None, window_height=None):
        if window_width is None:
            raise RuntimeError("GameManager window_width cannot be None")
        if window_height is None:
            raise RuntimeError("GameManager window_width cannot be None")
        self._window_width = window_width
        self._window_height = window_height
        self._player_character = PlayerCharacter(rect=(0, 0, PlayerCharacter.RECT_WIDTH, PlayerCharacter.RECT_HEIGHT))
        return

    def new_game(self):
        player_rect = self._player_character.get_rect()
        player_rect.centerx = self._window_width // 2
        player_rect.centery = self._window_height // 2
        return

    def get_player_character(self):
        return self._player_character

    def get_window_width(self):
        return self._window_width

    def get_window_height(self):
        return self._window_height
