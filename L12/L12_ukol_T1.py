from collections import deque
from datetime import datetime

class Pozadavek:
    def __init__(self, uzivatel):
        self.uzivatel = uzivatel
        self.casove_razitko = datetime.now()

class FrontaPozadavku:
    def __init__(self):
        self.fronta = deque()
        self.log_fronta = deque()

    def poslat_pozadavek(self, uzivatel):
        pozadavek = Pozadavek(uzivatel)
        self.fronta.append(pozadavek)2
        self.log_fronta.append((uzivatel, pozadavek.casove_razitko))
        print(f"Požadavek od uživatele {uzivatel} byl zařazen do fronty.")

    def zpracovat_pozadavek(self):
        if not self.fronta:
            print("Žádné požadavky k řešení.")
            return
        pozadavek = self.fronta.popleft()
        print(f"Zpracovávám požadavek od uživatele {pozadavek.uzivatel} z {pozadavek.casove_razitko}.")

    def zobrazit_statistiky(self):
        if not self.log_fronta:
            print("Žádné statistiky k zobrazení.")
            return
        print("Statistiky požadavků:")
        for uzivatel, cas in self.log_fronta:
            print(f"Uživatel: {uzivatel}, Čas: {cas}")

def zobrazit_menu():
    print("\n")
    print("Menu:")
    print("1. Poslat požadavek")
    print("2. Zpracovat požadavek")
    print("3. Zobrazit statistiky požadavků")
    print("4. Ukončit program")

def hlavni():
    fronta_pozadavku = FrontaPozadavku()
    while True:
        zobrazit_menu()
        volba = input("Zadejte volbu(1-4): ")

        if volba == '1':
            uzivatel = input("Zadejte uživatelské jméno: ")
            fronta_pozadavku.poslat_pozadavek(uzivatel)

        elif volba == '2':
            fronta_pozadavku.zpracovat_pozadavek()

        elif volba == '3':
            fronta_pozadavku.zobrazit_statistiky()

        elif volba == '4':
            print("KONEC")
            break
        else:
            print("Neplatná volba. Zvolte prosím platnou hodnotu znovu.")

if __name__ == "__main__":
    hlavni()