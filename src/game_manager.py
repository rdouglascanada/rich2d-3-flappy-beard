from pygame import Rect
from player_character import PlayerCharacter

class GameManager:
    def __init__(self):
        player_rect = Rect((0, 0, 50, 50))
        player_rect.centerx = 400
        player_rect.centery = 300
        self._player_character = PlayerCharacter(rect=player_rect)
        return

    def get_player_character(self):
        return self._player_character