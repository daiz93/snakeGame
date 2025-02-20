import pygame
import random

class Nourriture:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = self.spawn_food()

    def spawn_food(self):
        return [random.randrange(1, self.width // 10) * 10, random.randrange(1, self.height // 10) * 10]

    def draw(self, screen, color=(255, 0, 0)):
        pygame.draw.rect(screen, color, pygame.Rect(self.position[0], self.position[1], 10, 10))
        