import pygame
from random import sample
import time

class Gra():

    #stany gry
    POCZATEK = 0
    GRA = 1
    KONIEC = 2

    #ilość słów, które chcemy wyświetlać na ekranie
    ILOSC_SLOW = 5

    def __init__(self) -> None:
        self.wpisane_slowa = 0
        self.pisane_slowo = ""
        self.stan = 0
        self.poczatek_rozgrywki = time.time()

        self.slowa = []
        with open("slowa.txt", "r", encoding="UTF-8") as plik:
            self.slowa = [s.strip() for s in plik]

        self.wylosowane_slowa = sample(self.slowa, self.ILOSC_SLOW)

    def sprawdz_poprawnosc_slowa(self):
        if self.pisane_slowo in self.wylosowane_slowa:
            self.wylosowane_slowa.remove(self.pisane_slowo)
            self.pisane_slowo = ""
        if len(self.wylosowane_slowa) == 0:
            czas_rozgrywki = (time.time() - self.poczatek_rozgrywki) / 60
            self.slowa_na_minute = int(self.ILOSC_SLOW / czas_rozgrywki)
            try:
                with open("wyniki.txt", "r") as plik:
                    self.ostatni_wynik = plik.readline().strip()
            except:
                self.ostatni_wynik = "0"
            with open("wyniki.txt", "w") as plik:
                plik.write(str(self.slowa_na_minute))           
            self.stan = self.KONIEC

    def nacisnieto_klawisz(self, klawisz):
        if self.stan == self.POCZATEK:
            if klawisz == " ":
                self.stan = self.GRA
        elif self.stan == self.GRA:
            self.pisane_slowo += klawisz
            self.sprawdz_poprawnosc_slowa()
        elif self.stan == self.KONIEC:
            if klawisz == " ":
                exit(0)
        else:
            raise Exception("coś poszło bardzo nie tak")

    #funkcja obsługująca naciśnięcie klawisza backspace
    def usun_litere(self):
        if self.pisane_slowo:
            self.pisane_slowo = self.pisane_slowo[:-1]

    
