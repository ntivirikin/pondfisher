from models.game_map import GameMap

# Mangages interaction between player and map
class World:
    def __init__(self, player: Player, game_map: GameMap):
        self.player: Player = player
        self.pl_pos: list[int, int] = [0, 0]
        self.game_map: GameMap = game_map

    def get_pos(self) -> tuple[int, int]:
        return tuple(pl_pos[0], pl_pos[1])

