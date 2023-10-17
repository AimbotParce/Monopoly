from dataclasses import dataclass


@dataclass
class Player:
    name: str
    position: int = 0
    money: int = 1500
    jail_counter: int = 0  # How many turns the player has to stay in jail
    doubles_stack: int = 0  # How many doubles the player has rolled in a row

    def announce(self, message: str):
        print(f"[{self.name}] {message}")

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Player({self.name})"
