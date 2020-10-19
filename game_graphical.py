from random import randint
from math import cos
from math import sin
import pygame
pygame.init()

from player import *


def main():
    game_size = [600, 600]
    screen = pygame.display.set_mode(game_size)
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1.turn(-1)
        if keys[pygame.K_RIGHT]:
            player1.turn(1)
        if keys[pygame.K_UP]:
            player1.drive()

        screen.fill((230, 230, 230))
        draw_player(player1, screen)
        draw_player(player2, screen)
        pygame.display.flip()


    pygame.quit()

def draw_player(player, screen):
    pygame.draw.circle(screen, player.color, (int(player.position[0]), int(player.position[1])), player.size)
    pygame.draw.circle(screen, (0, 0, 0), (int(player.position[0] + cos(player.angle) * 15), int(player.position[1] + sin(player.angle) * 15)), 10)
    for bullet in player.bullets:
        pygame.draw.circle(screen, (0,0,0), (int(bullet.position[0]), int(bullet.position[1])), bullet.size)


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

        
