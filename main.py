import utils

from models.world import World
from models.game_map import GameMap


"""
    CLASSES
        > World: holds current map and location within it
            - player_name, location, current_map
        > Map: provides land and water grid 
            - map_name, width, height, grid

    STARTUP SEQUENCE
        > User input is requested to create World object
            - World("user_input") { player_name = user_input, current_map = default_map, location = (0, 0) }
"""


# Create world with default game map
def startup() -> World:
    utils.clear_console()
    try:
        name: str = input("Welcome to PondFisher! Enter your player name: ")
    except KeyboardInterrupt as e:
        print("Thanks for playing PondFisher!")
        exit()
    game_map: GameMap = GameMap("./data/pond_map.json")
    return World(name, game_map)


# Produces World and kicks off game loop
if __name__ == "__main__":

    world: World = startup()

    print("Thanks for playing PondFisher!")
