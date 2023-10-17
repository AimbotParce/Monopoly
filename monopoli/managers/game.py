from ..models.board import Board
from ..models.player import Player


class GameManager:
    def __init__(self, board: Board, players: list[Player] = []):
        self.board = board
        self.players = players
        self.current_player = 0
        self.round = 0

    def add_player(self, player: Player):
        self.players.append(player)
