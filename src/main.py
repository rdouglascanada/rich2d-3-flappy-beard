from rich2d.game import Game, GameConfig
from rich2d.audio import Music
from rich2d.models.ui import Button

background_music = Music("resources/luigi-boccherini-minuetto.mp3")
def toggle_music():
    if Music.is_any_music_playing():
        Music.stop_all_music()
    else:
        background_music.play_indefinitely()
    return

music_button = Button(rect=(660, 540, 120, 40), text="Toggle Music", on_left_mouse_click=toggle_music)

flappy_config = GameConfig(window_title="Flappy Beard", background_colour="skyblue",
                           window_width=800, window_height=600)
flappy_game = Game(model=music_button, config=flappy_config)
flappy_game.run()