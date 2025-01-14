import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Police pour le score
font = pygame.font.SysFont('Arial', 24)

# Paramètres du serpent
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = 'RIGHT'
change_to = snake_direction

# Vitesse initiale
speed = 10

# Paramètres de la nourriture
food_pos = [random.randrange(1, WIDTH//10) * 10, random.randrange(1, HEIGHT//10) * 10]
food_spawn = True

# Score
score = 0

# État de pause
paused = False

# Temps écoulé
start_time = pygame.time.get_ticks()

# Fonction d'affichage de l'écran de fin
def game_over():
    screen.fill(BLACK)
    game_over_text = font.render(f'Game Over! Score: {score}', True, WHITE)
    screen.blit(game_over_text, [WIDTH // 4, HEIGHT // 3])
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

# Fonction pour augmenter la difficulté
def increase_difficulty():
    global speed
    if score % 5 == 0:
        speed += 2

# Boucle principale
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            elif event.key == pygame.K_p:
                paused = not paused

    if paused:
        continue

    # Calcul du temps écoulé
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    # Validation de la direction
    if change_to == 'UP' and not snake_direction == 'DOWN':
        snake_direction = 'UP'
    if change_to == 'DOWN' and not snake_direction == 'UP':
        snake_direction = 'DOWN'
    if change_to == 'LEFT' and not snake_direction == 'RIGHT':
        snake_direction = 'LEFT'
    if change_to == 'RIGHT' and not snake_direction == 'LEFT':
        snake_direction = 'RIGHT'

    # Déplacement du serpent
    if snake_direction == 'UP':
        snake_pos[1] -= 10
    if snake_direction == 'DOWN':
        snake_pos[1] += 10
    if snake_direction == 'LEFT':
        snake_pos[0] -= 10
    if snake_direction == 'RIGHT':
        snake_pos[0] += 10

    # Ajout de la nouvelle position
    snake_body.insert(0, list(snake_pos))

    # Vérification de la collision avec la nourriture
    if snake_pos == food_pos:
        score += 1
        food_spawn = False
        increase_difficulty()
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, WIDTH//10) * 10, random.randrange(1, HEIGHT//10) * 10]
    food_spawn = True

    # Vérification de collision avec les murs ou le corps
    if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
        snake_pos in snake_body[1:]):
        game_over()

    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Affichage du score et du temps
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, [10, 10])
    time_text = font.render(f'Time: {elapsed_time}s', True, WHITE)
    screen.blit(time_text, [10, 40])

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()
