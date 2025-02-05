import pygame
import sys

from serpent import Serpent
from nourriture import Nourriture

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeux du serpent")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



# Police pour le score
font = pygame.font.SysFont('Arial', 24)

# Initialisation du serpent et de la nourriture
snake = Serpent()
food = Nourriture(WIDTH, HEIGHT)
# Home screen

screen.blit(pygame.image.load("welcome.png"), [0, 0])
pygame.display.flip()
pygame.time.wait(3000)

# Boucle principale
clock = pygame.time.Clock()
running = True



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction('UP')
            elif event.key == pygame.K_DOWN:
                snake.change_direction('DOWN')
            elif event.key == pygame.K_LEFT:
                snake.change_direction('LEFT')
            elif event.key == pygame.K_RIGHT:
                snake.change_direction('RIGHT')

    # Mise à jour du serpent
    snake.move()

    

pygame.quit()
sys.exit()
