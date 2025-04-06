from pygame import Rect

class PlayerCharacter:
    def __init__(self, rect=None):
        if rect is None:
            raise RuntimeError("PlayerCharacter rect cannot be None")
        self._rect = Rect(rect)
        return

    def get_rect(self):
        return self._rect