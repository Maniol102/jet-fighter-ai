import pygame
from player import *

from math import cos
from math import sin
from random import randint
from ConfigParser import SafeConfigParser



class Game:
    def __init__(self):
        parser = SafeConfigParser()
        parser.read('game.ini')

        self.game_size = [parser.get('GENERAL', 'game_size_w'), parser.get('GENERAL', 'game_size_h')]
        self.game_over = False

        self.player1 = Player([randint(0, self.game_size[0]), randint(0, self.game_size[1])], (255, 0, 0), 30, self.game_size)
        self.player2 = Player([randint(0, self.game_size[0]), randint(0, self.game_size[1])], (0, 0, 255), 30, self.game_size)

    def movement(self):
        self.player1.move()
        self.player2.move()

    def check_win(self, player):
        for i in player.bullets:
            if self.offScreen(i, self.game_size):
                player.bullets.remove(i)
            if self.intersect(i, player):
                player.bullets.remove(i)
                self.game_over = True
                return True

    def offScreen(self, obj, screensize):
        if obj.position[0] < 0:
            return True
        if obj.position[0] > screensize[0]:
            return True
        if obj.position[1] < 0:
            return True
        if obj.position[1] > screensize[1]:
            return True
        return False

    def intersect(self, bullet, player):
        if bullet.position[0] >= player.position[0]- 0.5 * player.size and \
        bullet.position[0] <= player.position[0] + 0.5 * player.size and \
        bullet.position[1] >= player.position[1] - 0.5 * player.size and \
        bullet.position[1] <= player.position[1] + 0.5 * player.size:
            return True
        return False

    def draw_player(self, player, screen):
        pygame.draw.circle(screen, player.color, (int(player.position[0]), int(player.position[1])), player.size)
        pygame.draw.circle(screen, (0, 0, 0), (int(player.position[0] + cos(player.angle) * 15), int(player.position[1] + sin(player.angle) * 15)), 10)
        for bullet in player.bullets:
            pygame.draw.circle(screen, (0,0,0), (int(bullet.position[0]), int(bullet.position[1])), bullet.size)

   