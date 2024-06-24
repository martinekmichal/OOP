class Kniha:
    def __init__(self, titul, rok_vydani, vydavatel, zanr, autor, cena):
        self.titul = titul
        self.rok_vydani = rok_vydani
        self.vydavatel = vydavatel
        self.zanr = zanr
        self.autor = autor
        self.cena = cena


    def n_titul(self, titul):
        self.titul = titul
    def n_rok_vydani(self, rok_vydani):
        self.rok_vydani = rok_vydani
    def n_vydavatele(self, vydavatel):
        self.vydavatel = vydavatel
    def n_zanr(self, zanr):
        self.zanr = zanr
    def n_autora(self, autor):
        self.autor = autor
    def n_cenu(self, cena):
        self.cena = cena


    def z_titul(self):
        return self.titul
    def z_rok_vydani(self):
        return self.rok_vydani
    def z_vydavatele(self):
        return self.vydavatel
    def z_zanr(self):
        return self.zanr
    def z_autora(self):
        return self.autor
    def z_cenu(self):
        return self.cena

    def z_info(self):
        return (f"Titul: {self.titul}, Rok vydání: {self.rok_vydani}, "
                f"Vydavatel: {self.vydavatel}, Žánr: {self.zanr}, "
                f"Autor: {self.autor}, Cena: {self.cena} Kč")


kniha = Kniha("Žert", 1974, "Albatros", "Drama", "Milan Kundera", 999)
print(kniha.z_info())

kniha.n_cenu(499)
kniha.n_zanr("Romace")
kniha.n_rok_vydani(1984)
print(kniha.z_info())