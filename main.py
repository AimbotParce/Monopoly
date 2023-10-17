from monopoli import GameManager, Player, VersionChoice

if __name__ == "__main__":
    board = VersionChoice("america")
    game = GameManager(board=board)
    game.add_player(Player("Player 1"))
    game.add_player(Player("Player 2"))
    print(board)
