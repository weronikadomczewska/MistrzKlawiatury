import pygame
from random import choice
from gra import Gra

class Interfejs():

    ROZMIAR_CZCIONKI_SLOWA = 14
    ROZMIAR_CZCIONKI_POLECENIA = 20
    TYP_CZCIONKI = "couriernew"
    SZEROKOSC = 600
    WYSOKOSC = 400
    KOLOR_TLA = "#121212"
    KOLOR_LITER = "#9AE66E"
    
    def __init__(self, gra : Gra) -> None:

        pygame.init()

        #tworzenie i edycja okna gry
        
        pygame.font.init()
        self.czcionka = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI_SLOWA)
        self.okno = pygame.display.set_mode((self.SZEROKOSC, self.WYSOKOSC))
        self.okno.fill(self.KOLOR_TLA)
        pygame.display.set_caption("Mistrz Klawiatury")

        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
            
        #     self.okno.fill(self.KOLOR_TLA)
        #     self.wyswietl_slowo("ala", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_SLOWA, 0, 0)
        #     pygame.display.update()

    def petla_gry(self):

        while True:
            # NOTE: obsługujemy zdarzenia
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.gra.nacisnieto_klawisz(event.key)
        
            # NOTE: na podstawie stanu gry rysujemy konkretną scenę
            if self.gra.stan == Gra.POCZATEK:
                self.rysuj_scene_poczatek(self, self.gra)
            elif self.gra.stan == Gra.GRA:
                self.rysuj_scene_gra(self, self.gra)
            elif self.gra.stan == Gra.KONIEC:
                self.rysuj_scene_koniec(self, self.gra)
            else:
                raise Exception("błędny stan, coś jest nie tak")
        
            # NOTE: jak już narysowaliśmy, to RAZ wyświetlamy to co narysowaliśmy
            pygame.display.update()
                

    def wyswietl_slowo(self, slowo, rodzaj_czcionki, rozmiar_czcionki,  x, y):
        self.czcionka = pygame.font.SysFont(rodzaj_czcionki, rozmiar_czcionki)
        napis = self.czcionka.render(slowo, True, self.KOLOR_LITER)
        self.okno.blit(napis, (x, y))

    def rysuj_scene_poczatek(self, gra):
        self.wyswietl_slowo("Mistrz Klawiatury!", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, 20, 20)

    def rysuj_scene_gra(self, gra):
        pass

    def rysuj_scene_koniec(self, gra):
        pass





