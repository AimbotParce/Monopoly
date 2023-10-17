from .square import Square


class Board:
    def __init__(self):
        self._board: list[Square] = []

    def add_square(self, square: Square):
        self._board.append(square)

    def get_square(self, index: int) -> Square:
        return self._board[index]

    def get_square_by_name(self, name: str) -> Square:
        for square in self._board:
            if square.name == name:
                return square
        raise ValueError(f"Square {name} not found")

    def get_square_index(self, square: Square) -> int:
        return self._board.index(square)

    def __getitem__(self, index: int) -> Square:
        return self.get_square(index)

    def __len__(self) -> int:
        return len(self._board)

    def __iter__(self):
        return iter(self._board)

    def __contains__(self, square: Square) -> bool:
        return square in self._board

    def __repr__(self) -> str:
        return f"Board({self._board})"

    def __str__(self) -> str:
        return "Monopoli(%s)" % ", ".join([str(square) for square in self._board])
