from enum import Enum, auto


class Color(Enum):
    BROWN = auto()
    LIGHT_BLUE = auto()
    PINK = auto()
    ORANGE = auto()
    RED = auto()
    YELLOW = auto()
    GREEN = auto()
    DARK_BLUE = auto()

    RAILROAD = auto()
    UTILITY = auto()
    CHANCE = auto()
    COMMUNITY_CHEST = auto()
    TAX = auto()
    SPECIAL = auto()


class Fore:
    white = "\033[37m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    orange = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    lightgrey = "\033[37m"
    darkgrey = "\033[90m"
    lightred = "\033[91m"
    lightgreen = "\033[92m"
    yellow = "\033[93m"
    lightblue = "\033[94m"
    pink = "\033[95m"
    lightcyan = "\033[96m"


fore = {
    Color.BROWN: Fore.purple,
    Color.LIGHT_BLUE: Fore.cyan,
    Color.PINK: Fore.pink,
    Color.ORANGE: Fore.orange,
    Color.RED: Fore.lightred,
    Color.YELLOW: Fore.yellow,
    Color.GREEN: Fore.green,
    Color.DARK_BLUE: Fore.blue,
    Color.RAILROAD: Fore.white,
    Color.UTILITY: Fore.white,
    Color.CHANCE: Fore.darkgrey,
    Color.COMMUNITY_CHEST: Fore.darkgrey,
    Color.TAX: Fore.darkgrey,
    Color.SPECIAL: Fore.darkgrey,
}
