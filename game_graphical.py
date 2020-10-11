from random import randint
from math import cos
from math import sin
import pygame
pygame.init()

from player import *

game_size = [600, 600]
screen = pygame.display.set_mode(game_size)
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

    pygame.draw.circle(screen, player1.color, (int(player1.position[0]), int(player1.position[1])), player1.size)
    pygame.draw.circle(screen, (0, 0, 0), (int(player1.position[0] + cos(player1.angle) * 15), int(player1.position[1] + sin(player1.angle) * 15)), 10)

    pygame.draw.circle(screen, player2.color, (int(player2.position[0]), int(player2.position[1])), player2.size)
    pygame.draw.circle(screen, (0, 0, 0), (int(player2.position[0] + cos(player2.angle) * 15), int(player2.position[1] + sin(player2.angle) * 15)), 10)

    for bullet in player1.bullets:
        pygame.draw.circle(screen, (0,0,0), (int(bullet.position[0]), int(bullet.position[1])), bullet.size)

    pygame.display.flip()
    
    


pygame.quit()


        
