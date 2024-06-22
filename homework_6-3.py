class Vehicle:
    
    vehicle_type = "none"

class Car:
    price = 1000000
    def __init__(self):

    def horse_powers(self):
        print(f'количество лошадиных сил: {self}')

class Nissan(Car, Vehicle):
    def __init__(self, price):
        super().horse_powers()
         vehicle_type =
        print(f'{self.vehicle_type}\n{self.price}')

