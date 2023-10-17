from ...models.player import Player


def go_to_jail(where: int = 10):
    def func(player: Player, announcer=print):
        player.position = where
        player.jail_counter = 3
        announcer("Go to jail! You are now in jail for 3 turns!")

    return func
