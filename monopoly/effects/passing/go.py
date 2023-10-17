from ...models.player import Player


def collect_go(ammount: int = 200):
    def func(player: Player, announcer=print):
        player.money += ammount
        announcer("You received $200 for passing GO!")

    return func
