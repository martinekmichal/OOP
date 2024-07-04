class Fronta:
    def __init__(self, velikost):
        self.fronta = []
        self.velikost = velikost

    def je_prazdna(self):
        return len(self.fronta) == 0
    def je_plna(self):
        return len(self.fronta) == self.velikost
    def vlozit(self, hodnota):
        if self.je_plna():
            print("Fronta je plná. Hodnotu nelze vložit.")
        else:
            self.fronta.append(hodnota)
            print(f"Vložena hodnota: {hodnota} do fronty.")
    def odebrat(self):
        if self.je_prazdna():
            print("Fronta je prázdná. Nelze odebrat hodnotu.")
            return None
        else:
            hodnota = self.fronta.pop()
            print(f"Odebrána hodnota: {hodnota} z fronty.")
            return hodnota

    def zobrazit(self):
        if self.je_prazdna():
            print("Fronta je prázdná.")
        else:
            print(f"Obsah fronty je: {self.fronta}")

def zobraz_menu():
    print("\nMenu:")
    print("1. Vložit do fronty")
    print("2. Odebrat z fronty")
    print("3. Zkontrolovat, zda je fronta prázdná")
    print("4. Zkontrolovat, zda je fronta plná")
    print("5. Zobrazit všechno ve frontě")
    print("6. Ukončit")

def hlavni():
    velikost = int(input("Zadejte velikost fronty: "))
    fronta = Fronta(velikost)

    while True:
        zobraz_menu()
        volba = input("Zvolte(1-6): ")

        if volba == '1':
            hodnota = input("Zadejte znak pro vložení do fronty: ")
            if len(hodnota) == 1:
                fronta.vlozit(hodnota)
            else:
                print("Zadejte jenom jeden znak!!!!")
        elif volba == '2':
            fronta.odebrat()
        elif volba == '3':
            if fronta.je_prazdna():
                print("Fronta je prázdná.")
            else:
                print("Fronta není prázdná.")
        elif volba == '4':
            if fronta.je_plna():
                print("Fronta je plná.")
            else:
                print("Fronta není plná.")
        elif volba == '5':
            fronta.zobrazit()
        elif volba == '6':
            print("KONEC")
            break
        else:
            print("Špatné zadání. Opakujte volbu prosím!")

if __name__ == "__main__":
    hlavni()