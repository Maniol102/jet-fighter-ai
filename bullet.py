from math import sqrt

class Bullet:
    def __init__(self, position, direction, size, speed):
        self.position = position
        self.direction = direction
        self.size = size
        self.speed = speed
        self.velocity = ((self.direction[0]/sqrt(self.direction[0]**2 + self.direction[1]**2))*self.speed, (self.direction[1]/sqrt(self.direction[0]**2 + self.direction[1]**2))*self.speed)

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
