class Serpent:
    def __init__(self, position=[100, 50], body=None, direction='RIGHT'):
        if body is None:
            body = [[100, 50], [90, 50], [80, 50]]
        self.position = position
        self.body = body
        self.direction = direction
        self.change_to = direction
        self.score = 0
        self.speed = 15

    def deplacer(self):
        # Mise à jour de la position de la tête
        self.x += self.dx
        self.y += self.dy

        # Ajout de la nouvelle position de la tête
        self.corps.insert(0, (self.x, self.y))

        # Suppression de la dernière partie du corps si le serpent ne grandit pas
        if len(self.corps) > self.longueur:
            self.corps.pop()
    def dessiner(self, fenetre):
        for segment in self.corps:
            pygame.draw.rect(fenetre, vert, (*segment, self.taille, self.taille))

    def grandir(self):
        self.longueur += 1

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