from rich2d.models import Model, ModelGroup
from rich2d.audio import Music
from rich2d.models.ui import Button
from rich2d.sprites.text import Text
from rich2d.handlers import MouseHandler
from rich2d.elements.animated_text import FlashingText

def intro_state(game_state):
    text_sprite = Text(text="Click to begin flapping",
                       rect=(200, 400, 400, 100),
                       font_name="helvetica",
                       font_size=48)
    flashing_element = FlashingText(text_sprite=text_sprite,
                                    flashes_per_interval=2, flash_interval=3)

    def set_play_state():
        game_state.set_value("play")
        return

    click_handler = MouseHandler(on_left_mouse_click=set_play_state)

    intro_model = Model(sprites=[text_sprite], elements=[flashing_element], handlers=[click_handler])
    return intro_model

def play_state(game_state):
    background_music = Music("resources/luigi-boccherini-minuetto.mp3")

    text_sprite = Text(text="Right click to end game",
                       rect=(200, 400, 400, 100),
                       font_name="helvetica",
                       font_size=48)

    def toggle_music():
        if Music.is_any_music_playing():
            Music.stop_all_music()
        else:
            background_music.play_indefinitely()
        return

    def set_game_over_state():
        game_state.set_value("game_over")
        Music.stop_all_music()
        return

    click_handler = MouseHandler(on_right_mouse_click=set_game_over_state)

    static_model = Model(sprites=[text_sprite], handlers=[click_handler])
    music_button = Button(rect=(20, 20, 120, 40), text="Toggle Music", on_left_mouse_click=toggle_music)
    return ModelGroup(models=[static_model, music_button])

def game_over_state(game_state):
    text_sprite = Text(text="Click to go back to start",
                       rect=(200, 400, 400, 100),
                       font_name="helvetica",
                       font_size=48)

    def set_intro_state():
        game_state.set_value("intro")
        Music.stop_all_music()
        return

    click_handler = MouseHandler(on_left_mouse_click=set_intro_state)

    static_model = Model(sprites=[text_sprite], handlers=[click_handler])
    return static_model