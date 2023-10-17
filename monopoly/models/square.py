from dataclasses import dataclass, field
from typing import Callable

from colorama import Style

from ..colors import Color, fore
from .player import Player


@dataclass
class Square:
    name: str
    color: Color
    landing_effects: list[Callable] = field(default_factory=list)
    passing_effects: list[Callable] = field(default_factory=list)

    def land(self, player: Player, announcer=None):
        if announcer is None:
            announcer = player.announce
        for effect in self.landing_effects:
            effect(player, announcer=announcer)

    def pass_by(self, player: Player, announcer=None):
        if announcer is None:
            announcer = player.announce
        for effect in self.passing_effects:
            effect(player, announcer=announcer)

    def __str__(self) -> str:
        return f"{fore[self.color]}{self.name}{Style.RESET_ALL}"

    def __repr__(self) -> str:
        return self.name
