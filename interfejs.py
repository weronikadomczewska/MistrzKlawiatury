import pygame
from gra import Gra

class Interfejs():

    ROZMIAR_CZCIONKI_SLOWA = 20
    ROZMIAR_CZCIONKI_POLECENIA = 24
    TYP_CZCIONKI = "couriernew"
    SZEROKOSC_OKNA = 600
    WYSOKOSC_OKNA = 400
    KOLOR_TLA = "#181818"
    KOLOR_LITER = "#C7F994"
    
    def __init__(self, gra : Gra) -> None:

        pygame.init()

        #system wysyła litery, którym odpowiadają klawisze na klawiaturze
        pygame.key.start_text_input()

        #tworzenie i edycja okna gry
        
        pygame.font.init()
        self.czcionka_mala = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI_SLOWA)
        self.czcionka_duza = pygame.font.SysFont("couriernew", self.ROZMIAR_CZCIONKI_POLECENIA)
        self.okno = pygame.display.set_mode((self.SZEROKOSC_OKNA, self.WYSOKOSC_OKNA))
        self.okno.fill(self.KOLOR_TLA)
        pygame.display.set_caption("Mistrz Klawiatury")

        self.petla_gry(gra)

    def petla_gry(self, gra : Gra):
        while True:
            # NOTE: obsługujemy zdarzenia
            for zdarzenie in pygame.event.get():
                if zdarzenie.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if zdarzenie.type == pygame.KEYDOWN and zdarzenie.key == pygame.K_BACKSPACE:
                    gra.usun_litere()
                if zdarzenie.type == pygame.TEXTINPUT:
                    gra.nacisnieto_klawisz(zdarzenie.text)
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
        
    def szerokosc_napisu(self, slowo, mala_czcionka=True):
        if mala_czcionka:
            napis = self.czcionka_mala.render(slowo, True, self.KOLOR_LITER)
        else:
            napis = self.czcionka_duza.render(slowo, True, self.KOLOR_LITER)
        return napis.get_width()

    def rysuj_scene_poczatek(self):
        self.okno.fill(self.KOLOR_TLA)
        szerokosc_tytul = self.szerokosc_napisu("MISTRZ KLAWIATURY", False)
        self.wyswietl_slowo("MISTRZ KLAWIATURY", self.SZEROKOSC_OKNA // 2 - szerokosc_tytul // 2, self.WYSOKOSC_OKNA // 3, False)
        szerokosc_komunikat = self.szerokosc_napisu("NACIŚNIJ SPACJĘ, ŻEBY ROZPOCZĄĆ", False)
        self.wyswietl_slowo("NACIŚNIJ SPACJĘ, ŻEBY ROZPOCZĄĆ", self.SZEROKOSC_OKNA // 2 - szerokosc_komunikat // 2, self.WYSOKOSC_OKNA // 2, False)
        
    def rysuj_scene_gra(self, gra : Gra):
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

        #rysowanie text boxa
        szerokosc_pisane_slowo = self.szerokosc_napisu(gra.pisane_slowo)
        tekst_x = self.SZEROKOSC_OKNA // 2 - szerokosc_pisane_slowo // 2
        tekst_y = self.WYSOKOSC_OKNA - (self.WYSOKOSC_OKNA // 5 - self.WYSOKOSC_OKNA // 10)

        self.wyswietl_slowo(gra.pisane_slowo, tekst_x, tekst_y)

    def rysuj_scene_koniec(self, gra):
        self.okno.fill(self.KOLOR_TLA)

        szerokosc_koniec_gry = self.szerokosc_napisu("KONIEC GRY", False)
        self.wyswietl_slowo("KONIEC GRY", self.SZEROKOSC_OKNA // 2 - szerokosc_koniec_gry // 2, self.WYSOKOSC_OKNA // 3, False)

        szerokosc_wpm = self.szerokosc_napisu("Słowa na minutę (WPM):")
        self.wyswietl_slowo(f"Słowa na minutę (WPM): {gra.slowa_na_minute}", self.SZEROKOSC_OKNA // 2 - szerokosc_wpm // 2, self.WYSOKOSC_OKNA // 3 + self.WYSOKOSC_OKNA // 10)

        szerokosc_ostatni_wynik = self.szerokosc_napisu(f"Ostatni wynik: {gra.ostatni_wynik}")
        self.wyswietl_slowo(f"Ostatni wynik: {gra.ostatni_wynik}", self.SZEROKOSC_OKNA // 2 - szerokosc_ostatni_wynik // 2, self.WYSOKOSC_OKNA // 3 + 2 * self.WYSOKOSC_OKNA // 10)

        szerokosc_wyjscie = self.szerokosc_napisu("NACIŚNIJ SPACJĘ, ABY WYJŚĆ", False)
        self.wyswietl_slowo("NACIŚNIJ SPACJĘ, ABY WYJŚĆ", self.SZEROKOSC_OKNA // 2 - szerokosc_wyjscie // 2, self.WYSOKOSC_OKNA // 3 + 3 * self.WYSOKOSC_OKNA // 10, False)

