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

        napis = self.czcionka.render("To be", True, self.KOLOR_LITER, self.KOLOR_TLA)
        napis1 = self.czcionka.render("or not to be", True, self.KOLOR_LITER, self.KOLOR_TLA)

        while True:
            self.okno.blit(napis, (0, 0))
            self.okno.blit(napis1, (50, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    def wyswietl_slowa(self, slowa):
        wysokosc_litery = self.WYSOKOSC - 50
        przesuniecie = 10






