import pygame
import sys
from serpent import Serpent
from nourriture import Nourriture

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Police pour le score
font = pygame.font.SysFont('Arial', 24)

# Initialisation du serpent et de la nourriture
snake = Serpent()
food = Nourriture(WIDTH, HEIGHT)

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

    # Vérification de la collision avec la nourriture
    if snake.body[0] == food.position:
        snake.has_eaten = True
        snake.score += 1
        snake.speed += 1
        food.position = food.spawn_food()

    # Vérification des collisions
    if snake.check_collision(WIDTH, HEIGHT, []):
        running = False

    # Affichage
    screen.fill(BLACK)
    snake.draw(screen)
    food.draw(screen)

    # Affichage du score
    score_text = font.render(f'Score: {snake.score}', True, WHITE)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()
    clock.tick(snake.speed)

pygame.quit()
sys.exit()
