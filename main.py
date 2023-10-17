from monopoly import GameManager, Player, VersionChoice

if __name__ == "__main__":
    board = VersionChoice("madrid")
    game = GameManager(board=board)
    game.add_player(Player("Player 1"))
    game.add_player(Player("Player 2"))
    game.print_board()
    while True:
        input()
        game.play_one_move()
