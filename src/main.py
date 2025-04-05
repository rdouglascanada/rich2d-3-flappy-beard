from rich2d.game import Game, GameConfig
from rich2d.models.state import StateModel, State
from states import intro_state, play_state, game_over_state

game_state = State(value="intro")
state_map = {
    "intro": intro_state(game_state),
    "play": play_state(game_state),
    "game_over": game_over_state(game_state)
}
game_model = StateModel(state=game_state, state_map=state_map)

flappy_config = GameConfig(window_title="Flappy Beard", background_colour="skyblue",
                           window_width=800, window_height=600)
flappy_game = Game(model=game_model, config=flappy_config)
flappy_game.run()