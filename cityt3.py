class Country:
    def __init__(self, country_name, continent, population, calling_code, capital, city_names):
        self.country_name = country_name
        self.continent = continent
        self.population = population
        self.calling_code = calling_code
        self.capital = capital
        self.city_names = city_names


    def set_country_name(self, country_name):
        self.country_name = country_name
    def set_continent(self, continent):
        self.continent = continent
    def set_population(self, population):
        self.population = population
    def set_calling_code(self, calling_code):
        self.calling_code = calling_code
    def set_capital(self, capital):
        self.capital = capital
    def set_city_names(self, city_names):
        self.city_names = city_names


    def get_country_name(self):
        return self.country_name
    def get_continent(self):
        return self.continent
    def get_population(self):
        return self.population
    def get_calling_code(self):
        return self.calling_code
    def get_capital(self):
        return self.capital
    def get_city_names(self):
        return self.city_names


    def display_info(self):
        print(f"Country Name: {self.country_name}")
        print(f"Continent: {self.continent}")
        print(f"Population: {self.population}")
        print(f"Calling Code: {self.calling_code}")
        print(f"Capital: {self.capital}")
        print(f"City Names: {', '.join(self.city_names)}")


country = Country(
    "Česká republika",
    "Evropa",
    10700000,
    "+420",
    "Praha",
    ["Praha", "Brno", "Ostrava", "Plzeň"]
)
country.display_info()

# Změna některých údajů
country.set_population(10800000)
country.set_city_names(["Praha", "Brno", "Ostrava", "Plzeň", "Liberec"])

print("\nAktualizované údaje:")
country.display_info()