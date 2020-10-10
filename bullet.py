from math import sqrt

class Bullet:
    def __init__(self, position, velocity, size, speed):
        self.position = position
        self.size = size
        self.speed = speed
        self.velocity = [velocity[0] * self.speed, velocity[1] * self.speed]

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
