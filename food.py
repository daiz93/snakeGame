import pygame
import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)

    def spawn(self):
        self.position = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.position[0], self.position[1], 10, 10))
