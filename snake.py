import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "RIGHT"
        self.grow = False

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10
        
        new_head = (x, y)
        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def change_direction(self, direction):
        opposite = {"UP": "DOWN", "DOWN": "UP", "LEFT": "RIGHT", "RIGHT": "LEFT"}
        if direction != opposite.get(self.direction, ""):
            self.direction = direction

    def grow_snake(self):
        self.grow = True

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:]
    
    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0], segment[1], 10, 10))
