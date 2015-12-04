class Car:
    def __init__(self, color, car_type, km):
        if type(color) != str:
            print()
        self.color = color
        self.type = car_type
        self.km = km

    def ride(self, km):
        self.km += km

    def getMiles(self):
        return self.km * 0.6213

tesla = Car("pink", "Tesla 5", 1200)

tesla.ride(220)

print(tesla.km)
