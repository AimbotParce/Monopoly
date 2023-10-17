from ..models.board import Board
from .america import board as america
from .madrid import board as madrid


class VersionChoice(Board):
    """Choose a version of Monopoly to play."""

    _map = {
        "america": america,
        "madrid": madrid,
    }

    def __new__(cls, version: str):
        if version not in VersionChoice._map:
            raise ValueError(f"Version {version} does not exist.")
        return VersionChoice._map[version]


__all__ = ["VersionChoice", "america"]
