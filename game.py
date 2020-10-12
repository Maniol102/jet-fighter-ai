from random import randint
from math import cos
from math import sin

from player import *
def main():
    game_size = [600, 600]
    game_over = False

    player1 = Player([randint(0, game_size[0]), randint(0, game_size[1])], (255, 0, 0), 30, game_size)
    player2 = Player([randint(0, game_size[0]), randint(0, game_size[1])], (0, 0, 255), 30, game_size)


    while not game_over:
        player1.move()
        player2.move()

        for i in player1.bullets:
            if i.position[0] < 0:
                player1.bullets.remove(i)
            if i.position[0] > game_size[0]:
                player1.bullets.remove(i)
            if i.position[1] < 0:
                player1.bullets.remove(i)
            if i.position[1] > game_size[1]:
                player1.bullets.remove(i)
            if (i.position[0] >= player2.position[0] - 0.5 * player2.size):
                if (i.position[0] <= player2.position[0] + 0.5 * player2.size):
                    if (i.position[1] >= player2.position[1] - 0.5 * player2.size):
                        if (i.position[1] <= player2.position[1] + 0.5 * player2.size):
                            player1.bullets.remove(i)
                            game_over = True
                            print("Player1 won")
        
        for i in player2.bullets:
            if i.position[0] < 0:
                player2.bullets.remove(i)
            if i.position[0] > game_size[0]:
                player2.bullets.remove(i)
            if i.position[1] < 0:
                player2.bullets.remove(i)
            if i.position[1] > game_size[1]:
                player2.bullets.remove(i)
            if i.position[0] >= player1.position[0] - 0.5 * player1.size:
                if i.position[0] <= player1.position[0] + 0.5 * player1.size:
                    if i.position[1] >= player1.position[1] - 0.5 * player1.size:
                        if i.position[1] <= player1.position[1] + 0.5 * player1.size:
                            player2.bullets.remove(i)
                            game_over = True
                            print("Player2 won")



main()