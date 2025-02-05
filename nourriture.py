import pygame
import random

class Nourriture:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = self.spawn_food()

    def spawn_food(self):
        pass

    def draw(self, screen, color=(255, 0, 0)):
        pass
        