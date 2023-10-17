from .colors import Color
from .models.square import Square

GO = Square("Go", Color.SPECIAL)
JAIL = Square("Jail", Color.SPECIAL)
FREE_PARKING = Square("Free Parking", Color.SPECIAL)
TO_JAIL = Square("Go to Jail", Color.SPECIAL)

COMMUNITY_CHEST = Square("Community Chest", Color.COMMUNITY_CHEST)
INCOME_TAX = Square("Income Tax", Color.TAX)
LUXURY_TAX = Square("Luxury Tax", Color.TAX)
CHANCE = Square("Chance", Color.CHANCE)

# Utilities
ELECTRIC_COMPANY = Square("Electric Company", Color.UTILITY)
WATER_WORKS = Square("Water Works", Color.UTILITY)
