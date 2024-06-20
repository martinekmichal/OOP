from my_error import MyCustomError
class Zlomek:
    def __init__(self, citatel=0, jmenovatel=1):
        self.citatel = citatel
        self.jmenovatel = jmenovatel

        if jmenovatel == 0:
            print("Jmenovatel nesmí být nula.")
            return
        else:
            return
    def nastav_citatel(self, citatel):
        self.citatel = citatel
    def nastav_jmenovatel(self, jmenovatel):
        self.jmenovatel = jmenovatel
        if jmenovatel == 0:
            print("Jmenovatel nesmí být nula.")
            return
        else:
            return

    def ziskej_citatel(self):
        return self.citatel
    def ziskej_jmenovatele(self):
        return self.jmanovatel

    def vypis(self):
        print(f"{self.citatel} / {self.jmenovatel}")

    def scitej(self, jiny):
        novy_citatel = self.citatel * jiny.jmenovatel + jiny.citatel * self.jmenovatel
        novy_jmenovatel = self.jmenovatel * jiny.jmenovatel
        return Zlomek(novy_citatel, novy_jmenovatel)

zlomek1 = Zlomek(1, 2)
zlomek2 = Zlomek(2, 2)

zlomek1.vypis()
zlomek2.vypis()

print()
try:
    soucet = zlomek1.scitej(zlomek2)
    soucet.vypis()
except:
    MyCustomError