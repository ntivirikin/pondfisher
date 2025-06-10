from models.player import Player
from models.game_map import GameMap


def create_player() -> Player:
    return Player(name)


def create_map() -> GameMap:
    return GameMap("./data/pond_map.json")


# Create player, map and world
def startup() -> World:
    name: str = input("Welcome to Heron! Enter your player name: ")
    player: Player = create_player(name)
    game_map: GameMap = create_map()
    return World(player, game_map)


if __name__ == "__main__":
    world: World = startup()
