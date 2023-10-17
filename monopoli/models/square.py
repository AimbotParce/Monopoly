from dataclasses import dataclass, field
from typing import Callable

from colorama import Style

from ..colors import Color, fore


@dataclass
class Square:
    name: str
    color: Color
    landing_effects: list[Callable] = field(default_factory=list)

    def __str__(self) -> str:
        return f"{fore[self.color]}{self.name}{Style.RESET_ALL}"
