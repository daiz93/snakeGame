import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.running = True
        self.paused = False
        self.score = 0
        self.speed = 10

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
                elif event.key == pygame.K_p:
                    self.paused = not self.paused

    def update(self):
        if not self.paused:
            self.snake.move()

            # Vérifier si le serpent mange la nourriture
            if self.snake.body[0] == self.food.position:
                self.snake.grow_snake()
                self.food.spawn()
                self.score += 10
                if self.score % 50 == 0:
                    self.speed += 1

            # Vérifier les collisions
            x, y = self.snake.body[0]
            if x < 0 or x >= 400 or y < 0 or y >= 400 or self.snake.check_collision():
                self.running = False

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        
        font = pygame.font.Font(None, 30)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        if self.paused:
            pause_text = font.render("PAUSE", True, (255, 255, 255))
            self.screen.blit(pause_text, (170, 180))

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.speed)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
