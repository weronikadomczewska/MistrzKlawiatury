import pygame

class Interfejs():
    
    def __init__(self) -> None:
        self.szerokosc = 600
        self.wysokosc = 400
        self.kolor_tla = "#121212"

        okno = pygame.display.set_mode((self.szerokosc, self.wysokosc))
        pygame.display.set_caption("Mistrz Klawiatury")
        okno.fill(self.kolor_tla)

        gra_dziala = True
        while gra_dziala:
            for zdarzenie in pygame.event.get():
                if zdarzenie.type == pygame.QUIT:
                    gra_dziala = False

        if not gra_dziala:
            pygame.display.flip()




