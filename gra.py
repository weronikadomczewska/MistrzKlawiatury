class Gra():

    SLOWA = []
    with open("slowa.txt", "r", encoding="UTF-8") as plik:
        SLOWA = [s.strip() for s in plik]

    POCZATEK = 0
    GRA = 1
    KONIEC = 2

    def __init__(self) -> None:
        self.wpisane_slowa = 0
        self.niepoprawne_slowa = 0
        self.poprawne_slowa = 0
        self.slowa_na_minute = 0
        self.klawisze_na_minute = 0
        self.pisane_slowo = 0
        self.teksty_na_ekranie = []

    
