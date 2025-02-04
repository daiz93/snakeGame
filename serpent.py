class Serpent:
    def __init__(self):
        self.taille = 20
        self.x = largeur_fenetre // 2
        self.y = hauteur_fenetre // 2
        self.dx = 0
        self.dy = 0
        self.corps = [(self.x, self.y)]
        self.longueur = 1

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

        