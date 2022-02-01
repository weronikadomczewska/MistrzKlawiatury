import pygame

class Gra():

    POCZATEK = 0
    GRA = 1
    KONIEC = 2

    def __init__(self) -> None:
        self.wpisane_slowa = 0
        self.slowa_na_minute = 0
        self.pisane_slowo = ""
        self.teksty_na_ekranie = []
        self.stan = 0

        self.slowa = []
        with open("slowa.txt", "r", encoding="UTF-8") as plik:
            self.slowa = [s.strip() for s in plik]

    def nacisnieto_klawisz(self, klawisz):
        if self.stan == self.POCZATEK:
            if klawisz == pygame.K_SPACE:
                self.stan = self.GRA
        elif self.stan == self.GRA:
            if len(self.teksty_na_ekranie) == 0:
                self.stan = self.KONIEC
        elif self.stan == self.KONIEC:
            if klawisz == pygame.K_SPACE:
                self.stan = self.POCZATEK
        else:
            raise Exception("coś poszło bardzo nie tak")

    
