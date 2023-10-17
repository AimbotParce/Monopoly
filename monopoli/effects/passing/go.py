from ...models.player import Player


def receive_go(player: Player, ammount: int = 200, announcer=print):
    player.money += ammount
    announcer("You received $200 for passing GO!")
