import pygame

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


    def deplacer(self):
        # Mise à jour de la position de la tête
        self.x += self.dx
        self.y += self.dy

        # Ajout de la nouvelle position de la tête
        self.corps.insert(0, (self.x, self.y))

        # Suppression de la dernière partie du corps si le serpent ne grandit pas
        if len(self.corps) > self.longueur:
            self.corps.pop()
    def draw(self, screen, color=(0, 255, 0)):
        for pos in self.body:
            pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], 10, 10))
    def change_direction(self, new_direction): 
        if new_direction == 'UP' and self.direction != 'DOWN':
            self.change_to = 'UP'
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.change_to = 'DOWN'
        elif new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.change_to = 'LEFT'
        elif new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.change_to = 'RIGHT'

    def move(self):
        self.direction = self.change_to
        if self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'RIGHT':
            self.position[0] += 10

        self.body.insert(0, list(self.position))

        # Supprime le dernier segment du corps si le serpent n'a pas mangé
        if not hasattr(self, 'has_eaten') or not self.has_eaten:
            self.body.pop()
        else:
            self.has_eaten = False  # Réinitialise l'état après avoir grandi


    def grandir(self):
        self.longueur += 1
    def grow(self):
        # Ne pas retirer la dernière partie du corps pour que le serpent grandisse
        pass

    def collision_avec_bordure(self):
        return self.x < 0 or self.x >= WIDTH or self.y < 0 or self.y >= HEIGHT

    def collision_avec_soi_meme(self):
        return (self.x, self.y) in self.corps[1:]
    
    def check_collision(self, width, height, obstacles):
        if (self.position[0] < 0 or self.position[0] >= width or
            self.position[1] < 0 or self.position[1] >= height or
            self.position in self.body[1:] or
            self.position in obstacles):
            return True
        return False
    
    def move(self):
        self.direction = self.change_to
        if self.direction == 'UP':
            self.position[1] -= 10
        elif self.direction == 'DOWN':
            self.position[1] += 10
        elif self.direction == 'LEFT':
            self.position[0] -= 10
        elif self.direction == 'RIGHT':
            self.position[0] += 10

        self.body.insert(0, list(self.position))

        # Supprime le dernier segment du corps si le serpent n'a pas mangé
        if not hasattr(self, 'has_eaten') or not self.has_eaten:
            self.body.pop()
        else:
            self.has_eaten = False  # Réinitialise l'état après avoir grandi

