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
        > Game loop begins after world creation, user is presented with commands
            - Move, Quit
            - If none of the above, give error message and restart loop
        > One of four actions is performed, state is updated, game loop restarts
"""


def quit_game():
    print("Thanks for playing PondFisher!")
    exit() # Would typically call a shutdown/teardown function




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


# Produces world and kicks off game loop
if __name__ == "__main__":

    # Startup
    world: World = startup()

    # Dictionary to hold all possible moves and commands
    COMMANDS = {
        "m": world.move_pl,
        "q": quit_game
    }

    # Game loop
    while True:
        try:
            command: str = input("What would you like to do now? (M)ove, (d)ig, or (q)uit?\n")
        except KeyboardInterrupt as e:
            print("Error encountered, exiting...")
            exit()

        action = COMMANDS.get(command)
        if action:
            result = action()

        else:
            print("Command not known, please try again.")

