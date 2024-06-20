class Human:
    def __init__(self, name, birth, number=None):
        self.name = name
        self.birth = birth
        self.number = number

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

h1 = Human("Adam", "20.9.1999")
h2 = Human("Eva", "15.3.1992")
h2 = Human("Eva", "15.3.1992")



"""
h1 = Human("Adam", "20.9.1999")
h2 = Human("Eva", "15.3.1992")

print(h1)
print(h2)
"""