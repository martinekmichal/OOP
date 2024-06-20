class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def __str__(self):
        return f"""
    Name:    {self.name}
    Country: {self.country}"""


    def __eq__(self, other):
        return self.name == other.name and self.country == other.country



c1 = City("Praha", "česko")
c2 = City("Berlin", "nemecko")

print(c1)
print(c2)
print("prag" == "prag")
print(c1 == c2)
c2.name = c1.name
c2.country = c1.country
print(c1 == c2)