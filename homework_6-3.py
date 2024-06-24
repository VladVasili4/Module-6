"""Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
 которая возвращает количество лошидиных сил для автомобиля
Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
а также переопределите функцию horse_powers
Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price"""


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = "none"


class Car:
    def __init__(self, price, power):
        self.price = 1000000
    def horse_powers(self, power):
        self.power = power
        print(f'количество лошадиных сил: {self.power}')


class Nissan(Vehicle, Car):
    def __init__(self, vehicle_type, price):
        self.vehicle_type = 'sedan'
        self.price = 1200999
        # self.power = 111
        super().horse_powers(111)




almera = Nissan('vaz', 333)
print(f'{almera.vehicle_type}\n{almera.price}')
print(Nissan.mro())