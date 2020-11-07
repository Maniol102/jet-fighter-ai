from player import *
from game import *
from displaying import *


def main():
    game = Game()
    screen = Screen()
    while True:
        if not game.game_over:
            game.movement()
            game.check_win(game.player1)
            game.check_win(game.player2)

            screen.check_events()
            screen.render(game)

        else:
            break
main()
        