class City:
    def __init__(self, city_name, region_name, country_name, number_of_citizens, zip_code, area_code):
        self.city_name = city_name
        self.region_name = region_name
        self.country_name = country_name
        self.number_of_citizens = number_of_citizens
        self.zip_code = zip_code
        self.area_code = area_code

# pro zadavani hodnot (nástup)
    def set_city_name(self, city_name):
        self.city_name = city_name
    def set_region_name(self,region_name):
        self.region_name = region_name
    def set_country_name(self, country_name):
        self.country_name = country_name
    def set_number_of_citizens(self, number_of_citizens):
        self.number_of_citizens = number_of_citizens
    def set_zip_code(self, zip_code):
        self.zip_code = zip_code
    def set_area_code(self, area_code):
        self.area_code = area_code

# pro dávání hodnot (výstup)

    def get_city_name(self):
        return self.city_name
    def get_region_name(self):
        return self.region_name
    def get_country_name(self):
        return self.country_name
    def get_number_of_citizens(self):
        return self.number_of_citizens
    def get_zip_code(self):
        return self.zip_code
    def get_area_code(self):
        return self.area_code

    def print_seznam(self):
        print(f"Jméno města: {self.city_name}")
        print(f"Název regionu: {self.region_name}")
        print(f"Název Země: {self.country_name}")
        print(f"Příslušnost: {self.number_of_citizens}")
        print(f"PSČ: {self.zip_code}")
        print(f"Kód oblasti: {self.area_code}"),


city = City("Praha", "Hlavní město Praha", "Česká republika", 1300000, "11000", "2")
city.print_seznam()

city.set_number_of_citizens("česká")
city.set_zip_code("76843")

print("\nAktualizované údaje:")
city.print_seznam()