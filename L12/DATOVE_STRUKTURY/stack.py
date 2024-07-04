

class Stack:

    def __init__(self, size):
        self.size = size
        self.__stack= []

    def push(self, value):
        if len(self.__stack) < self.size:
            self.__stack.append(value)
            return True
        return False
    def pop(self):
        if len(self.__stack) > 0:
           self.__stack.pop()  #odebírá od konce (pop)
           return
        return None
    def count(self):
        return len(self.__stack)
    def is_empty(self):
        return len(self.__stack) == 0
    def is_full(self):
        return len(self.__stack) == self.size
    def clear(self):
        self.__stack = []
        print("Zasobník vymazaný.")
    def peek(self):
        if self.is_empty():
            print("Zásobník prázdný.")
            return None
        else:
            return self.__stack[-1]
def display_menu():
    print("\nMenu:")
    print("1. Vložit  číslo!")
    print("2. Vyjmout poslední číslo číslo!")
    print("3. Počet čísel!")
    print("4. Je prázdný?")
    print("5. Je plný?")
    print("6. Vymazat!")
    print("7. Zobraz na poslední číslo!")
    print("8. Konec")

def main():
    size = int(input("Zadej velikost: "))
    stack = Stack(size)

    while True:
        display_menu()
        choice = input("Vyber operaci (1-8): ")

        if choice == '1':
            value = int(input("Zadej celé číslo pro vložení: "))
            stack.push(value)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            print(f"V zásobníku je {stack.count()} čísel.")
        elif choice == '4':
            if stack.is_empty():
                print("Zásobník je prázdný.")
            else:
                print("Zásobník není prázdný")
        elif choice == '5':
            if stack.is_full():
                print("Zásobník je plný.")
            else:
                print("Zasobník není plný.")
        elif choice == '6':
            stack.clear()
        elif choice == '7':
            value = stack.peek()
            if value is not None:
                print(f"Poslední číslo v zásobníku je {value}.")
        elif choice == '8':
            print("KONEC")
            break
        else:
            print("Neplatná volba! Zvolte operaci znovu (1-8).")

if __name__ == "__main__":
    main()
