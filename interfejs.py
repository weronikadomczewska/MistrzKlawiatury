import pygame
from random import choice
from gra import Gra

class Interfejs():

    ROZMIAR_CZCIONKI_SLOWA = 20
    ROZMIAR_CZCIONKI_POLECENIA = 20
    TYP_CZCIONKI = "couriernew"
    SZEROKOSC_OKNA = 600
    WYSOKOSC_OKNA = 400
    KOLOR_TLA = "#181818"
    KOLOR_LITER = "#C7F994"
    
    def __init__(self, gra : Gra) -> None:

        pygame.init()

        #tworzenie i edycja okna gry
        
        pygame.font.init()
        self.czcionka_mala = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI_SLOWA)
        self.czcionka_duza = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI_POLECENIA)
        self.okno = pygame.display.set_mode((self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA))
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
                
    def wyswietl_slowo(self, slowo, x, y, mala_czcionka=True):
        if mala_czcionka:
            napis = self.czcionka_mala.render(slowo, True, self.KOLOR_LITER)
        else:
            napis = self.czcionka_duza.render(slowo, True, self.KOLOR_LITER)
        self.okno.blit(napis, (x, y))

    def rysuj_scene_poczatek(self):
        self.okno.fill(self.KOLOR_TLA)
        self.wyswietl_slowo("MISTRZ KLAWIATURY", self.SZEROKOSC_OKNA // 3, self.WYSOKOSC_OKNA // 10)
        self.wyswietl_slowo("Naciśnij spację, aby rozpocząć", self.SZEROKOSC_OKNA // 5, self.WYSOKOSC_OKNA // 2, False)

    def rysuj_scene_gra(self, gra):
        self.okno.fill(self.KOLOR_TLA)
        pygame.draw.line(self.okno, self.KOLOR_LITER, (0, self.WYSOKOSC_OKNA - self.WYSOKOSC_OKNA // 5), (self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA - self.WYSOKOSC_OKNA //5))

        x = 0
        y = 0

        for slowo in gra.wylosowane_slowa:
 
            napis = self.czcionka_mala.render(slowo + " ", True, self.KOLOR_LITER)
            szerokosc_slowa = napis.get_width()
            wysokosc_slowa = napis.get_height()

            if x + szerokosc_slowa >= self.SZEROKOSC_OKNA:
                y += wysokosc_slowa 
                x = 0

            self.wyswietl_slowo(slowo + " ", x, y)
            x += szerokosc_slowa

    def rysuj_scene_koniec(self, gra):
        self.okno.fill(self.KOLOR_TLA)
        self.wyswietl_slowo("KONIEC GRY", self.SZEROKOSC_OKNA // 2 - self.SZEROKOSC_OKNA // 8, self.WYSOKOSC_OKNA // 10, False)
        self.wyswietl_slowo(f"Słowa na minutę (WPM): {gra.wpisane_slowa // 60}", self.SZEROKOSC_OKNA // 2 - self.SZEROKOSC_OKNA // 4, self.WYSOKOSC_OKNA // 5, False)

        try:
            ostatni_wynik = ""
            with open("wyniki.txt", "r") as plik:
                ostatni_wynik = plik.readline().strip()
        except:
            ostatni_wynik = "0"

        self.wyswietl_slowo(f"Słowa na minutę (WPM): {gra.slowa_na_minute}", self.SZEROKOSC_OKNA // 2 - self.SZEROKOSC_OKNA // 4, self.WYSOKOSC_OKNA // 5, False)
        self.wyswietl_slowo(f"Ostatni wynik: {ostatni_wynik}", self.SZEROKOSC_OKNA // 2 - self.SZEROKOSC_OKNA // 4, self.WYSOKOSC_OKNA // 3, False)

        self.wyswietl_slowo("NACIŚNIJ SPACJĘ, ABY ZAGRAĆ PONOWNIE", self.SZEROKOSC_OKNA // 2 - self.SZEROKOSC_OKNA // 3, self.WYSOKOSC_OKNA // 2 + self.WYSOKOSC_OKNA // 3, False)

        with open("wyniki.txt", "w") as plik:
            plik.write(str(gra.slowa_na_minute))
