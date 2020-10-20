from random import randint
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
            if offScreen(i, game_size):
                player1.bullets.remove(i)
            if intersect(i, player2):
                player1.bullets.remove(i)
                game_over = True
                print("Player1 won")
        
        for i in player2.bullets:
            if offScreen(i, game_size):
                player2.bullets.remove(i)
            if intersect(i, player2):
                player2.bullets.remove(i)
                game_over = True
                print("Player2 won")


def offScreen(obj, screensize):
    if obj.position[0] < 0:
        return True
    if obj.position[0] > screensize[0]:
        return True
    if obj.position[1] < 0:
        return True
    if obj.position[1] > screensize[1]:
        return True
    return False


def intersect(bullet, player):
    if bullet.position[0] >= player.position[0]- 0.5 * player.size and \
    bullet.position[0] <= player.position[0] + 0.5 * player.size and \
    bullet.position[1] >= player.position[1] - 0.5 * player.size and \
    bullet.position[1] <= player.position[1] + 0.5 * player.size:
        return True
    return False

main()