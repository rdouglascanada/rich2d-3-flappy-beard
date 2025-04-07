from rich2d.models import Model
from rich2d.sprites.images import Image, ImageSprite
from rich2d.elements import Element

class FloorModel(Model):
    def __init__(self, game_manager=None):
        if game_manager is None:
            raise RuntimeError("CardSprite game_manager cannot be None")
        floor_image = Image.load_from_file("resources/ground.png")

        self._game_manager = game_manager
        floor_width = game_manager.get_window_width()
        floor_sprite = ImageSprite(image=floor_image, rect=(0, 500, floor_width, 100))
        floor_sprite_copy = ImageSprite(image=floor_image, rect=(floor_width, 500, floor_width, 100))

        def sync_rects():
            player_character = game_manager.get_player_character()
            player_rect = player_character.get_rect()
            floor_x = -(player_rect.x % floor_width)
            floor_sprite_rect = floor_sprite.get_rect()
            floor_sprite_rect.x = floor_x
            floor_sprite_copy_rect = floor_sprite_copy.get_rect()
            floor_sprite_copy_rect.x = floor_width + floor_x
            return

        sync_element = Element(on_update=sync_rects)

        super().__init__(sprites=[floor_sprite, floor_sprite_copy], elements=[sync_element])
        return