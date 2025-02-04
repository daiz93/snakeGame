import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def update(self):
        self.snake.move()

        # Vérifier si le serpent mange la nourriture
        if self.snake.body[0] == self.food.position:
            self.snake.grow_snake()
            self.food.spawn()

        # Vérifier les collisions
        x, y = self.snake.body[0]
        if x < 0 or x >= 400 or y < 0 or y >= 400 or self.snake.check_collision():
            self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)
        pygame.quit()
