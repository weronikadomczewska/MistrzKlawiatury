import pygame
from random import choice
from gra import Gra

class Interfejs():

    ROZMIAR_CZCIONKI = 14
    SZEROKOSC = 600
    WYSOKOSC = 400
    KOLOR_TLA = "#121212"
    KOLOR_LITER = "#9AE66E"
    
    def __init__(self, gra : Gra) -> None:

        pygame.init()

        #tworzenie i edycja okna gry
        
        pygame.font.init()
        self.czcionka = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI)
        self.okno = pygame.display.set_mode((self.SZEROKOSC, self.WYSOKOSC))
        self.okno.fill(self.KOLOR_TLA)
        pygame.display.set_caption("Mistrz Klawiatury")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            
            self.okno.fill(self.KOLOR_TLA)
            self.wyswietl_slowa("ala", 0, 0)
            pygame.display.update()
                

    def wyswietl_slowa(self, slowo, x, y):
        napis = self.czcionka.render(slowo, True, self.KOLOR_LITER)
        self.okno.blit(napis, (x, y))






