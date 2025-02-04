class Nourriture:
    def __init__(self):
        self.taille = TAILLE_SERPENT
        self.x = random.randrange(0, WIDTH, self.taille)
        self.y = random.randrange(0, HEIGHT, self.taille)

    def dessiner(self, fenetre):
        pygame.draw.rect(fenetre, RED, (self.x, self.y, self.taille, self.taille))

    def repositionner(self):
        self.x = random.randrange(0, WIDTH, self.taille)
        self.y = random.randrange(0, HEIGHT, self.taille)