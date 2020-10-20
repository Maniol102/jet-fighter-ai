from math import cos
from math import sin
from bullet import *

class Player:
    def __init__(self, position, color, size, gs):
        self.position = position
        self.color = color
        self.size = size
        self.velocity = [0, 0]
        self.turn_velocity = .004
        self.angle = 90
        self.speed = 0.004
        self.bullets = []
        self.game_size = gs

    def move(self):
        self.velocity[0] *= 0.99
        self.velocity[1] *= 0.99
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        for i in self.bullets:
            i.move()

        if self.position[0] >= self.game_size[0]:
            self.position[0] -= self.game_size[0]
        if self.position[0] <= 0:
            self.position[0] += self.game_size[0]
        if self.position[1] >= self.game_size[1]:
            self.position[1] -= self.game_size[1]
        if self.position[1] <= 0:
            self.position[1] += self.game_size[1]
            

    def drive(self):
        self.velocity[0] += cos(self.angle) * self.speed
        self.velocity[1] += sin(self.angle) * self.speed
    
    def turn(self, direction):
        self.angle += direction*self.turn_velocity
    
    def shoot(self):
        self.bullets.append(Bullet([self.position[0], self.position[1]], [cos(self.angle), sin(self.angle)], 5, 0.5))
