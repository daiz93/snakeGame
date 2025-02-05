import pygame

class Serpent:
    def __init__(self, position=[100, 50], body=None, direction='RIGHT'):
        if body is None:
            body = [[100, 50], [90, 50], [80, 50]]
        self.position = position
        self.body = body
        self.direction = direction
        self.change_to = direction
        self.score = 0
        self.speed = 5

 