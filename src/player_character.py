from pygame import Rect

class PlayerCharacter:
    RECT_WIDTH = 50
    RECT_HEIGHT = 50
    ACCELERATION_DUE_TO_GRAVITY = 0.2
    TERMINAL_VELOCITY = 2
    FLAP_VELOCITY = -2

    def __init__(self, rect=None, velocity=0):
        if rect is None:
            raise RuntimeError("PlayerCharacter rect cannot be None")
        self._rect = Rect(rect)
        self._velocity = velocity
        return

    def get_rect(self):
        return self._rect

    def get_velocity(self):
        return self._velocity

    def move(self):
        self._velocity += PlayerCharacter.ACCELERATION_DUE_TO_GRAVITY
        self._velocity = min(self._velocity, PlayerCharacter.TERMINAL_VELOCITY)

        self._rect.x += 1
        self._rect.y += self._velocity
        return

    def flap(self):
        self._velocity = PlayerCharacter.FLAP_VELOCITY
        return