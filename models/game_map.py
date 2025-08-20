import json

class GameMap:
    def __init__(self, map_path: str):
        map_data: dict = self.load_map(map_path)

        self.map_name: str = map_data["name"]
        self.height: int = map_data["height"]
        self.width: int = map_data["width"]
        self.grid: list[list[int]] = map_data["grid"]


    def load_map(self, map_path: str) -> dict:
        with open(map_path, 'r') as file:
            data = json.load(file)
        return data


    def bound_check(self, x: int, y: int) -> bool:
        if (x < 0) or (x > (self.height - 1)):
            return False
        
        if (y < 0) or (y > (self.width - 1)):
            return False

        if self.grid[x][y] == 1:
            return False
            
        return True 
