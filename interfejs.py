import pygame
from random import choice

class Interfejs():

    SLOWA = []
    with open("slowa.txt", "r", encoding="UTF-8") as plik:
        SLOWA = [s.strip() for s in plik]

    ROZMIAR_CZCIONKI = 14
    
    def __init__(self) -> None:
        self.szerokosc = 600
        self.wysokosc = 400
        self.kolor_tla = "#121212"
        self.kolor_liter = "#9AE66E"

        pygame.font.init()
        self.czcionka = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI)
        self.okno = pygame.display.set_mode((self.szerokosc, self.wysokosc))

        pygame.init()

        #tworzenie i edycja okna gry
        pygame.display.set_caption("Mistrz Klawiatury")
        self.okno.fill(self.kolor_tla)
        
        napis = self.czcionka.render("Happy birthday", True, self.kolor_liter, self.kolor_tla)
        napis1 = self.czcionka.render("To you!", True, self.kolor_liter, self.kolor_tla)



        while True:
            self.okno.blit(napis, (0, 0))
            self.okno.blit(napis1, (50, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pygame.display.update()

    def wyswietl_slowa(self, slowa):
        wysokosc_litery = self.wysokosc - 50
        przesuniecie = 10






