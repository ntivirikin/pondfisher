from models.game_map import GameMap



# Manages interactions with the map
class World:
    def __init__(self, pl_name: str, game_map: GameMap):
        self.pl_name: str = pl_name
        self.pl_pos: tuple[int, int] = (0, 0)
        self.game_map: GameMap = game_map


    # Get and set player position
    def get_pos(self) -> tuple[int, int]:
        return (self.pl_pos[0], self.pl_pos[1])

    def set_pos(self, new_x, new_y) -> None:
        self.pl_pos = (new_x, new_y)


    # Represent the direction we have to add to location to get new location
    DIRECTIONS = {
        "n": (-1, 0),
        "s": (1, 0),
        "w": (0, -1),
        "e": (0, 1)
    }

    # Moves the player if game map bounds allow for it
    def move_pl(self):
        try:
            direction: str = input("What direction? (N)orth, (S)outh, (E)ast or (W)est?").lower()
        except KeyboardInterrupt as e:
            print("Exiting now...")
            exit()

        # Check if input is a direction
        loc_add: tuple[int, int] | None = self.DIRECTIONS.get(direction)
        if not loc_add:
            print("Invalid direction! Please use n, s, e or w.")
            return False

        # Form the new coordinates
        new_x: int = self.get_pos()[0] + loc_add[0]
        new_y: int = self.get_pos()[1] + loc_add[1]

        # Check bounds using game map
        if not self.game_map.bound_check(new_x, new_y):
            print("Out of bounds, you cannot move there!")
            return False
        
        self.set_pos(new_x, new_y)

        return True
        

