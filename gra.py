import pygame
from random import choice
import time

class Gra():

    POCZATEK = 0
    GRA = 1
    KONIEC = 2

    def __init__(self) -> None:
        self.wpisane_slowa = 0
        self.pisane_slowo = ""
        self.stan = 0
        self.poczatek_rozgrywki = time.time()

        self.slowa = []
        with open("slowa.txt", "r", encoding="UTF-8") as plik:
            self.slowa = [s.strip() for s in plik]

        self.wylosowane_slowa = [choice(self.slowa) for i in range(50)]

    def nacisnieto_klawisz(self, klawisz):
        if self.stan == self.POCZATEK:
            if klawisz == " ":
                self.stan = self.GRA
        elif self.stan == self.GRA:
            self.pisane_slowo += klawisz
        elif self.stan == self.KONIEC:
            if klawisz == " ":
                exit(0)
        else:
            raise Exception("coś poszło bardzo nie tak")

    def usun_litere(self):
        if self.pisane_slowo:
            self.pisane_slowo = self.pisane_slowo[:-1]
    
