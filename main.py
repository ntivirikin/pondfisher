import utils

from models.world import World
from models.player import Player
from models.game_map import GameMap


def create_player(name: str) -> Player:
    return Player(name)


def create_map() -> GameMap:
    return GameMap("./data/pond_map.json")


# Create player, map and world
def startup() -> World:
    utils.clear_console()
    try:
        name: str = input("Welcome to PondFisher! Enter your player name: ")
    except KeyboardInterrupt as e:
        print("Thanks for playing PondFisher!")
        exit()
    player: Player = create_player(name)
    game_map: GameMap = create_map()
    return World(player, game_map)


if __name__ == "__main__":

    # Ask for name, produce the world
    world: World = startup()
    
    # Go into action loop
    world.act_loop()

    print("Thanks for playing PondFisher!")
