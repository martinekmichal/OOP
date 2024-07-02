import pickle

class Tvar:
    def zobraz(self):
        raise NotImplementedError("Tato metoda by měla být přepsána v odvozených třídách")

    def uloz(self, nazev_souboru):
        with open(nazev_souboru, "wb") as soubor:
            pickle.dump(self, soubor)

    @staticmethod
    def nacti(nazev_souboru):
        with open(nazev_souboru, "rb") as soubor:
            return pickle.load(soubor)

class Ctverec(Tvar):
    def __init__(self, x, y, strana):
        self.x = x
        self.y = y
        self.strana = strana

    def zobraz(self):
        print(f"Čtverec: Horní levý roh ({self.x}, {self.y}), Délka strany {self.strana}")

class Obdelnik(Tvar):
    def __init__(self, x, y, sirka, vyska):
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def zobraz(self):
        print(f"Obdélník: Horní levý roh ({self.x}, {self.y}), Šířka {self.sirka}, Výška {self.vyska}")

class Kruh(Tvar):
    def __init__(self, x, y, polomer):
        self.x = x
        self.y = y
        self.polomer = polomer

    def zobraz(self):
        print(f"Kruh: Střed ({self.x}, {self.y}), Poloměr {self.polomer}")

class Elipsa(Tvar):
    def __init__(self, x, y, sirka, vyska):
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska

    def zobraz(self):
        print(f"Elipsa: Horní levý roh ({self.x}, {self.y}), Šířka {self.sirka}, Výška {self.vyska}")

tvary = [Ctverec(1, 2, 5),
    Obdelnik(3, 4, 6, 7),
    Kruh(5, 6, 4),
    Elipsa(7, 8, 10, 5)]

nazev_souboru = "tvary.txt"
with open(nazev_souboru, "wb") as soubor:
    pickle.dump(tvary, soubor)

with open(nazev_souboru, "rb") as soubor:
    nactene_tvary = pickle.load(soubor)

for tvar in nactene_tvary:
    tvar.zobraz()