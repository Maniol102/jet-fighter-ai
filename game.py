from random import randint

from player import *

game_size = (400, 400)

player1 = Player((randint(0, game_size[0]), randint(0, game_size[1])), (255, 0, 0), 10)
player2 = Player((randint(0, game_size[0]), randint(0, game_size[1])), (0, 0, 255), 10)
