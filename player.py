import math

class Player:
    def __init__(self, position, color, size):
        self.position = position
        self.color = color
        self.size = size
        self.velocity = [0, 0]
        self.turn_velocity = 3
        self.angle = 0
        self.accel = [0, 0]
        self.speed = 5

    def move(self):
        self.velocity[0] += int(self.accel[0])
        self.velocity[1] += self.accel[1]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def drive(self):
        self.velocity[0] += math.cos(self.angle) * self.speed
        self.velocity[1] += math.sin(self.angle) * self.speed
    
    def turn(self):
        self.angle += self.turn_velocity
