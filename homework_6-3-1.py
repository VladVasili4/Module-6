"""Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию def horse_powers,
 которая возвращает количество лошидиных сил для автомобиля
Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
а также переопределите функцию horse_powers
Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price"""


class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self, power):
        self.power = power
        print(f'количество лошадиных сил: {self.power}')


class Nissan(Vehicle, Car):
    vehicle_type = 'sedan'
    price = 1200999

    def horse_powers(self, power):
        self.power = power
        print(f'количество лошадиных сил: {self.power}')


almera = Nissan()
almera.horse_powers(99)
print(f'{almera.vehicle_type}\n{almera.price}')
print(Nissan.mro())