from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def turn(self, direction):
        print(f"odbočím do {direction}")


