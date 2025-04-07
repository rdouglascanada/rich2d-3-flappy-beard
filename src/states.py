from rich2d.models import Model, ModelGroup
from rich2d.audio import Music
from rich2d.models.ui import Button
from rich2d.sprites.text import Text
from rich2d.handlers import MouseHandler
from rich2d.elements import Element
from rich2d.elements.animated_text import FlashingText
from player_model import PlayerModel
from floor_model import FloorModel

def intro_state(game_state, game_manager):
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

    flappy_model = PlayerModel(player_character=game_manager.get_player_character())
    floor_model = FloorModel(game_manager=game_manager)
    intro_model = Model(sprites=[text_sprite], elements=[flashing_element], handlers=[click_handler])
    return ModelGroup(models=[intro_model, floor_model, flappy_model])

def play_state(game_state, game_manager):
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

    def flap():
        player_character = game_manager.get_player_character()
        player_character.flap()
        return

    click_handler = MouseHandler(on_left_mouse_click=flap, on_right_mouse_click=set_game_over_state)

    def move_player_sprite():
        player_character = game_manager.get_player_character()
        player_character.move()
        return

    move_element = Element(on_update=move_player_sprite, time_interval=0.075)

    static_model = Model(sprites=[text_sprite], elements=[move_element], handlers=[click_handler])

    flappy_model = PlayerModel(player_character=game_manager.get_player_character())
    floor_model = FloorModel(game_manager=game_manager)
    music_button = Button(rect=(20, 20, 120, 40), text="Toggle Music", on_left_mouse_click=toggle_music)
    return ModelGroup(models=[static_model, music_button, floor_model, flappy_model])

def game_over_state(game_state, game_manager):
    text_sprite = Text(text="Click to go back to start",
                       rect=(200, 400, 400, 100),
                       font_name="helvetica",
                       font_size=48)

    def set_intro_state():
        game_manager.new_game()
        game_state.set_value("intro")
        Music.stop_all_music()
        return

    click_handler = MouseHandler(on_left_mouse_click=set_intro_state)

    static_model = Model(sprites=[text_sprite], handlers=[click_handler])
    floor_model = FloorModel(game_manager=game_manager)
    return ModelGroup(models=[static_model, floor_model])