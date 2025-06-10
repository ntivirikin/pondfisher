import utils

from models.game_map import GameMap
from models.player import Player

# Manages interaction between player and map, a session
class World:
    def __init__(self, player: Player, game_map: GameMap):
        self.player: Player = player
        self.pl_pos: list[int] = [0, 0]
        self.game_map: GameMap = game_map


    def get_pos(self) -> tuple[int, int]:
        return (self.pl_pos[0], self.pl_pos[1])


    # Player decides next action: Move, Dig, Fish, or Quit
    def act_loop(self) -> None:
        while True:
            utils.clear_console()
            try:
                action: str = input("What next? (m)ove, (d)ig, (f)ish, (q)uit.\n")
            except KeyboardInterrupt as e:
                print("Thanks for playing!")
                exit()

            if action == "m" or action == "M":
                self.move_player()
            elif action == "d" or action == "D":
                print("Dig!")
            elif action == "f" or action == "F":
                print("Fish!")
            elif action == "q" or action == "Q":
                break

    # Manages player movement
    def move_player(self) -> None:
        utils.clear_console()
        while True:
            print(f"Your position is: {self.get_pos()}")
            try:
                direct: str = input("\nWhat direction? (n)orth, (s)outh, (e)ast, (w)est, (q)uit moving.\n")
            except KeyboardInterrupt as e:
                print("Thanks for playing PondFisher!")
                exit()
            utils.clear_console()

            if direct in ['n', 'N']:
                if self.game_map.bound_check( self.get_pos()[0] - 1, self.get_pos()[1] ):
                    self.pl_pos[0] = self.pl_pos[0] - 1
                else:
                    print("Cannot go North! ")

            elif direct in ['s', 'S']:
                if self.game_map.bound_check( self.get_pos()[0] + 1, self.get_pos()[1] ):
                    self.pl_pos[0] = self.pl_pos[0] + 1
                else:
                    print("Cannot go South! ")

            elif direct in ['w', 'W']:
                if self.game_map.bound_check( self.get_pos()[0], self.get_pos()[1] - 1 ):
                    self.pl_pos[1] = self.pl_pos[1] - 1
                else:
                    print("Cannot go West! ")

            elif direct in ['e', 'E']:
                if self.game_map.bound_check( self.get_pos()[0], self.get_pos()[1] + 1 ):
                    self.pl_pos[1] = self.pl_pos[1] + 1
                else:
                    print("Cannot go East! ")

            elif direct in ['q', 'Q']:
                break
