from .. import common
from ..colors import Color
from ..models.board import Board
from ..models.square import Square

board = Board()

board.add_square(common.GO)
board.add_square(Square("Ronda de Valencia", Color.BROWN))
board.add_square(common.COMMUNITY_CHEST)
board.add_square(Square("Plaza de Lavapiés", Color.BROWN))
board.add_square(common.INCOME_TAX)
board.add_square(Square("Estación de Goya", Color.RAILROAD))
board.add_square(Square("Glorieta Cuatro Caminos", Color.LIGHT_BLUE))
board.add_square(common.CHANCE)
board.add_square(Square("Avenida de la Reina Victoria", Color.LIGHT_BLUE))
board.add_square(Square("Calle de Bravo Murillo", Color.LIGHT_BLUE))
board.add_square(common.JAIL)
board.add_square(Square("Glorieta de Bilbao", Color.PINK))
board.add_square(common.ELECTRIC_COMPANY)
board.add_square(Square("Calle de Alberto Aguilera", Color.PINK))
board.add_square(Square("Calle de Fuencarral", Color.PINK))
board.add_square(Square("Estación de las Delicias", Color.RAILROAD))
board.add_square(Square("Avenida de Felipe II", Color.ORANGE))
board.add_square(common.COMMUNITY_CHEST)
board.add_square(Square("Calle de Velázquez", Color.ORANGE))
board.add_square(Square("Calle de Serrano", Color.ORANGE))
board.add_square(common.FREE_PARKING)
board.add_square(Square("Avenida de América", Color.RED))
board.add_square(common.CHANCE)
board.add_square(Square("Calle de María de Molina", Color.RED))
board.add_square(Square("Calle de Cea Bermúdez", Color.RED))
board.add_square(Square("Estación del Mediodía", Color.RAILROAD))
board.add_square(Square("Avenida de los Reyes Católicos", Color.YELLOW))
board.add_square(Square("Calle de Bailén", Color.YELLOW))
board.add_square(common.WATER_WORKS)
board.add_square(Square("Plaza de España", Color.YELLOW))
board.add_square(common.TO_JAIL)
board.add_square(Square("Puerta del Sol", Color.GREEN))
board.add_square(Square("Calle de Alcalá", Color.GREEN))
board.add_square(common.COMMUNITY_CHEST)
board.add_square(Square("Gran Vía", Color.GREEN))
board.add_square(Square("Estación del Norte", Color.RAILROAD))
board.add_square(common.CHANCE)
board.add_square(Square("Paseo de la Castellana", Color.DARK_BLUE))
board.add_square(common.LUXURY_TAX)
board.add_square(Square("Paseo del Prado", Color.DARK_BLUE))
