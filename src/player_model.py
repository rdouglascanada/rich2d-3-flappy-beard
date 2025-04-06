from rich2d.models import Model
from rich2d.sprites.shapes import Rectangle
from rich2d.elements import Element

class PlayerModel(Model):
    def __init__(self, player_character=None):
        if player_character is None:
            raise RuntimeError("PlayerModel player_character cannot be None")

        player_sprite = Rectangle(rect=player_character.get_rect(), colour="orange")

        def sync_player_sprite():
            player_sprite.get_rect().update(player_character.get_rect())
            return

        player_element = Element(on_update=sync_player_sprite)

        super().__init__(sprites=[player_sprite], elements=[player_element])
        return