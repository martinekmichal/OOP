class Stadion:
    def __init__(self, nazev, datum_otevreni, zeme, mesto, kapacita):
        self.nazev = nazev
        self.datum_otevreni = datum_otevreni
        self.zeme = zeme
        self.mesto = mesto
        self.kapacita = kapacita

    def n_nazev(self, nazev):
        self.nazev = nazev
    def n_datum_otevreni(self, datum_otevreni):
        self.datum_otevreni = datum_otevreni
    def n_zemi(self, zeme):
        self.zeme = zeme
    def n_mesto(self, mesto):
        self.mesto = mesto
    def n_kapacitu(self, kapacita):
        self.kapacita = kapacita

    def z_nazev(self):
        return self.nazev
    def z_datum_otevreni(self):
        return self.datum_otevreni
    def z_zemi(self):
        return self.zeme
    def z_mesto(self):
        return self.mesto
    def z_kapacitu(self):
        return self.kapacita

    def z_info(self):
        return (f"Název: {self.nazev}, Datum otevření: {self.datum_otevreni}, "
                f"Země: {self.zeme}, Město: {self.mesto}, Kapacita: {self.kapacita} míst")


stadion = Stadion("Olomócký stadion", "1915", "Česká republika", "Olomouc", 150000)
print()
print(stadion.z_info())
stadion.n_kapacitu(199999)
print()
print(stadion.z_info())
stadion.n_nazev("Sigma stadion")
print()
print(stadion.z_info())
