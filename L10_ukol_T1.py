class Auto:
    def __init__(self, model, rok_vyroby, vyrobce, objem_motoru, barva, cena):
        self.model = model
        self.rok_vyroby = rok_vyroby
        self.vyrobce = vyrobce
        self.objem_motoru = objem_motoru
        self.barva = barva
        self.cena = cena

    def n_model(self, model):
        self.model = model
    def n_rok_vyroby(self, rok_vyroby):
        self.rok_vyroby = rok_vyroby
    def n_vyrobce(self, vyrobce):
        self.vyrobce = vyrobce
    def n_objem_motoru(self, objem_motoru):
        self.objem_motoru = objem_motoru
    def n_barvu(self, barva):
        self.barva = barva
    def n_cenu(self, cena):
        self.cena = cena


    def z_model(self):
        return self.model
    def z_rok_vyroby(self):
        return self.rok_vyroby
    def z_vyrobce(self):
        return self.vyrobce
    def z_objem_motoru(self):
        return self.objem_motoru
    def z_barvu(self):
        return self.barva
    def z_cenu(self):
        return self.cena

    def z_info(self):
        return (f"Model: {self.model}, Rok výroby: {self.rok_vyroby}, "
                f"Výrobce: {self.vyrobce}, Objem motoru: {self.objem_motoru} l, "
                f"Barva: {self.barva}, Cena: {self.cena} Kč")

auto = Auto("Octavia", 2023, "Škoda", 2.0, "modrá", 660000)

print(auto.z_info())
auto.n_cenu(760000)
auto.n_model("SuperB")
auto.n_barvu("Šedá")
print(auto.z_info())


