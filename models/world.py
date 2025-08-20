from models.game_map import GameMap

# Manages interaction between player and map, a session
class World:
    def __init__(self, pl_name: str, game_map: GameMap):
        self.pl_name: str = pl_name
        self.pl_pos: list[int] = [0, 0]
        self.game_map: GameMap = game_map


    def get_pos(self) -> tuple[int, int]:
        return (self.pl_pos[0], self.pl_pos[1])
