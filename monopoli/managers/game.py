from time import sleep

from colorama import Fore, Style

from ..common import JAIL
from ..format.message_box import get_msg_box
from ..models.board import Board
from ..models.player import Player


class GameManager:
    def __init__(self, board: Board, players: list[Player] = []):
        self._board = board
        self._players = players
        self._screen_messages = []
        self.current_player = 0
        self.round = 0

    def add_player(self, player: Player):
        self._players.append(player)

    def next_player(self):
        self._players[self.current_player].doubles_stack = 0
        self.current_player += 1
        if self.current_player >= len(self._players):
            self.current_player = 0
            self.round += 1

    def roll_dice(self) -> int:
        return self._board.roll_dice()

    def announce(self, msg: str, player: Player = None):
        if player is None:
            name = "Global"
        else:
            name = player.name
        text = f"[{name}] {msg}"
        self._screen_messages.append(text)

    def flush_messages(self):
        self._screen_messages.clear()

    def play_one_move(self):
        player = self._players[self.current_player]
        dice = self.roll_dice()
        is_double = len(set(dice)) == 1

        self.announce(f"You rolled {dice[0]} and {dice[1]}. For a total of {sum(dice)}", player=player)

        if player.jail_counter > 0:
            if is_double:
                self.announce("You rolled a double! You are free!", player=player)
                player.jail_counter = 0
            else:
                player.jail_counter -= 1
                self.announce(f"You are still in jail for {player.jail_counter} more turns!", player=player)
                return

        if is_double and player.doubles_stack == 2:
            self.announce("You rolled three doubles in a row! Go to jail!", player=player)
            player.position = self._board.get_square_index(JAIL)
            player.jail_counter = 3
            self._board[player.position].land(player)
            return

        for i in range(sum(dice)):
            player.position += 1
            if player.position >= len(self._board):
                player.position = 0
            self._board[player.position].pass_by(player)
            self.print_board()
        self._board[player.position].land(player)

        if is_double:
            self.announce("You rolled a double! Roll again!", player=player)
            self.print_board()
            player.doubles_stack += 1
        else:
            self.next_player()
            self.print_board()
            self.flush_messages()

    def print_board(self, sleep_time=0.1):
        players_on_each_square = [[] for _ in range(len(self._board))]
        for i, player in enumerate(self._players):
            if i == self.current_player:
                players_on_each_square[player.position].append(f"{Fore.GREEN}{str(player)}{Style.RESET_ALL}")
            else:
                players_on_each_square[player.position].append(str(player))

        # Print many empty lines to clear the screen
        msg = "\n" * 100
        msg += get_msg_box("\n".join(self._screen_messages), title="Messages") + "\n"

        board = [
            f"{str(square):<35s}: {', '.join(players)}" for players, square in zip(players_on_each_square, self._board)
        ]
        msg += "\n".join(board)
        print(msg)
        sleep(sleep_time)
