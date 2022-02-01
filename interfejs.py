import pygame
from random import choice
from gra import Gra

class Interfejs():

    ROZMIAR_CZCIONKI_SLOWA = 14
    ROZMIAR_CZCIONKI_POLECENIA = 20
    TYP_CZCIONKI = "couriernew"
    SZEROKOSC = 600
    WYSOKOSC = 400
    KOLOR_TLA = "#181818"
    KOLOR_LITER = "#C7F994"
    
    def __init__(self, gra : Gra) -> None:

        pygame.init()

        #tworzenie i edycja okna gry
        
        pygame.font.init()
        self.czcionka = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI_SLOWA)
        self.okno = pygame.display.set_mode((self.SZEROKOSC, self.WYSOKOSC))
        self.okno.fill(self.KOLOR_TLA)
        pygame.display.set_caption("Mistrz Klawiatury")

        self.petla_gry(gra)

    def petla_gry(self, gra):
        while True:
            # NOTE: obsługujemy zdarzenia
            for zdarzenie in pygame.event.get():
                if zdarzenie.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if zdarzenie.type == pygame.KEYDOWN:
                    gra.nacisnieto_klawisz(zdarzenie.key)
            # NOTE: na podstawie stanu gry rysujemy konkretną scenę
            if gra.stan == Gra.POCZATEK:
                self.rysuj_scene_poczatek()
            elif gra.stan == Gra.GRA:
                self.rysuj_scene_gra(gra)
            elif gra.stan == Gra.KONIEC:
                self.rysuj_scene_koniec(gra)
            else:
                raise Exception("błędny stan, coś jest nie tak")
        
            # NOTE: jak już narysowaliśmy, to RAZ wyświetlamy to co narysowaliśmy
            pygame.display.update()
                
    def wyswietl_slowo(self, slowo, rodzaj_czcionki, rozmiar_czcionki,  x, y):
        self.czcionka = pygame.font.SysFont(rodzaj_czcionki, rozmiar_czcionki)
        napis = self.czcionka.render(slowo, True, self.KOLOR_LITER)
        self.okno.blit(napis, (x, y))

    def rysuj_scene_poczatek(self):
        self.okno.fill(self.KOLOR_TLA)
        self.wyswietl_slowo("MISTRZ KLAWIATURY", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 3, self.WYSOKOSC // 10)
        self.wyswietl_slowo("Naciśnij spację, aby rozpocząć", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 5, self.WYSOKOSC // 2)

    def rysuj_scene_gra(self, gra):
        self.okno.fill(self.KOLOR_TLA)
        pygame.draw.line(self.okno, self.KOLOR_LITER, (0, self.WYSOKOSC - self.WYSOKOSC // 5), (self.SZEROKOSC, self.WYSOKOSC - self.WYSOKOSC //5))

        x = 0
        y = 0

        self.czcionka = pygame.font.SysFont(self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_SLOWA)

        for slowo in gra.wylosowane_slowa:
 
            napis = self.czcionka.render(slowo, True, self.KOLOR_LITER)
            szerokosc_slowa = napis.get_width()
            wysokosc_slowa = napis.get_height()

            maks_szerokosc = self.SZEROKOSC

            if maks_szerokosc <= szerokosc_slowa:
                y += wysokosc_slowa
                x = 0

            self.wyswietl_slowo(slowo, self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_SLOWA, x, y)
            maks_szerokosc -= szerokosc_slowa

            self.okno.blit(napis, (x, y))

    def rysuj_scene_koniec(self, gra):
        self.okno.fill(self.KOLOR_TLA)
        self.wyswietl_slowo("KONIEC GRY", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 2 - self.SZEROKOSC // 8, self.WYSOKOSC // 10)
        self.wyswietl_slowo(f"Słowa na minutę (WPM): {gra.wpisane_slowa // 60}", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 2 - self.SZEROKOSC // 4, self.WYSOKOSC // 5)

        try:
            ostatni_wynik = ""
            with open("wyniki.txt", "r") as plik:
                ostatni_wynik = plik.readline().strip()
        except:
            ostatni_wynik = "0"

        self.wyswietl_slowo(f"Słowa na minutę (WPM): {gra.slowa_na_minute}", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 2 - self.SZEROKOSC // 4, self.WYSOKOSC // 5)
        self.wyswietl_slowo(f"Ostatni wynik: {ostatni_wynik}", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 2 - self.SZEROKOSC // 4, self.WYSOKOSC // 3)

        self.wyswietl_slowo("NACIŚNIJ SPACJĘ, ABY ZAGRAĆ PONOWNIE", self.TYP_CZCIONKI, self.ROZMIAR_CZCIONKI_POLECENIA, self.SZEROKOSC // 2 - self.SZEROKOSC // 3, self.WYSOKOSC // 2 + self.WYSOKOSC // 3)

        with open("wyniki.txt", "w") as plik:
            plik.write(str(gra.slowa_na_minute))
