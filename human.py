class Human:
    def __init__(self, name, birth, number=None):
        self.__name = name # private
        self._number = number  # protected
        self.birth = birth # public

    def set_name(self, name):
        if len(name) < 3:
            return False

        self.__name = name
        return True


    def get_name(self):
        return self.__name


h1 = Human("adam", "20.9.1999")
h2 = Human("eva", "15.3.1992")
h3 = Human("eva", "15.3.1992")


#print(h1.__name)

h1.name = "karol"
print(h1.name)
print(h1.get_name())
h1.set_name("Vojta")
print(h1.get_name())





"""

print(h1)
print(h2)
print(h3)
print(h1 == h2)
print(h3 == h2)

print("------------------")
h1 = h2
print(h1)
print(h2)
print(h1 == h2)
"""