class City:
    def __init__(self, name, country):
        self.__name = name
        self.__country = country

    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self,value):
        self.__country = value

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def delete_city(self):
        print("Mažu se!")

    name = property(
        fget= get_name,
        fset= set_name,
        fdel= delete_city,
        doc="tot je jméno města"

    )

c1 = City("Praha", "Česko")
print(c1.name)
c1.name = "Berlín"

print(c1.name)

del c1.name
help(City.name)

