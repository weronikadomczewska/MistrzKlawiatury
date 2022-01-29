class Gra():

    SLOWA = []
    with open("slowa.txt", "r", encoding="UTF-8") as plik:
        SLOWA = [s.strip() for s in plik]

    def __init__(self) -> None:
        self.wpisane_slowa = 0
        self.niepoprawne_slowa = 0
        self.poprawne_slowa = 0
        self.slowa_na_minute = 0
        self.klawisze_na_minute = 0
        self.pisane_slowo = 0

    
# g = Gra()
# print(g.SLOWA)