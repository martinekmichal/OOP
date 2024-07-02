import math

class Kruh:
    def __init__(self, x, y, polomer):
        self.x = x
        self.y = y
        self.polomer = polomer

    def zobraz(self):
        print(f"Kruh: Střed ({self.x}, {self.y}), Poloměr {self.polomer}")

    def obvod(self):
        return 2 * math.pi * self.polomer

    def __eq__(self, jiny_kruh):
        return self.polomer == jiny_kruh.polomer

    def __gt__(self, jiny_kruh):
        return self.obvod() > jiny_kruh.obvod()

    def __lt__(self, jiny_kruh):
        return self.obvod() < jiny_kruh.obvod()

    def __ge__(self, jiny_kruh):
        return self.obvod() >= jiny_kruh.obvod()

    def __le__(self, jiny_kruh):
        return self.obvod() <= jiny_kruh.obvod()

    def __add__(self, hodnota):
        return Kruh(self.x, self.y, self.polomer + hodnota)

    def __sub__(self, hodnota):
        return Kruh(self.x, self.y, self.polomer - hodnota)

    def __iadd__(self, hodnota):
        self.polomer += hodnota
        return self

    def __isub__(self, hodnota):
        self.polomer -= hodnota
        return self

kruh1 = Kruh(0, 1, 5)
kruh2 = Kruh(1, 1, 10)
print(kruh1 == kruh2)

print(kruh1 > kruh2)
print(kruh1 < kruh2)
print(kruh1 >= kruh2)
print(kruh1 <= kruh2)


kruh3 = kruh1 + 3
kruh3.zobraz()

kruh4 = kruh2 - 2
kruh4.zobraz()

kruh1 += 2
kruh1.zobraz()

kruh2 -= 5
kruh2.zobraz()
