from my_error import MyCustomError

class Fraction:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        return f"{self.nominator}/{self.denominator}"

    def __eq__(self, other):
        return self.nominator * other.denominator == self.denominator * other.nominator

    def __add__(self, other):
        common_denominator = self.denominator * other.denominator
        new_nominator = self.nominator * other.denominator + other.nominator * self.denominator
        return Fraction(new_nominator, common_denominator)

    def __iadd__(self, o):
        if not isinstance(o, Fraction):
            raise MyCustomError("Unsupported operand type for +=: '{}' and '{}'".format(type(self), type(o)))

        common_denominator = self.denominator * o.denominator
        self.nominator = self.nominator * o.denominator + o.nominator * self.denominator
        self.denominator = common_denominator
        return self
"""(Button()
.set_color("red")
.set_radius(10))"""


f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
f3 = Fraction(2, 2)

print(f1 == f2)
f4 = f1 + f2
print(f4)
print(f4 == f3)

print(f1)
f1 += f2
print(f1)

print(isinstance(f1, Fraction))
try:
    f1 += 3
except MyCustomError:
    print("pokusil si sa scitat nekompatibilne typy")