from rich2d.game import Game, GameConfig

flappy_config = GameConfig(window_title="Flappy Beard", background_colour="skyblue",
                           window_width=800, window_height=600)
flappy_game = Game(config=flappy_config)
flappy_game.run()