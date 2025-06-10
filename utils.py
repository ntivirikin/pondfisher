import os

def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')