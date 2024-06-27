"""Атрибуты класса Figure: sides_count = 0
Каждый объект класса Figure должен обладать следующими атрибутами:
Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
Атрибуты(публичные): filled(закрашенный, bool)
И методами:
Метод get_color, возвращает список RGB цветов.
Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
Метод set_sides принимает неограниченное кол-во сторон, проверяет корректность переданных данных, если данные корректны, то меняет __sides на новый список, если нет, то оставляет прежние.
Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
Метод __len__ должен возвращать периметр фигуры.


Атрибуты класса Circle: sides_count = 1
Каждый объект класса Circle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).

Атрибуты класса Figure: sides_count = 3
Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure
Атрибут __height, высота треугольника (можно рассчитать зная все стороны треугольника)   (h = 2S / a)
S - площадьб а - длина основания
Метод get_square возвращает площадь треугольника.

Атрибуты класса Figure: sides_count = 12
Каждый объект класса Cube должен обладать следующими атрибутами и методами:
Все атрибуты и методы класса Figure.
Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
Метод get_volume, возвращает объём куба.

ВАЖНО!
При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count, то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]"""
import math



class Figure:
    r, g, b = 0, 0, 0           # черный
    sides_count = 0

    def __init__(self, *sides, color):
        r, g, b = 0, 0, 0

        if self.__isvalid_sides(*sides):
            self.__sides = sides
        else: [1] * self.sides_count            # ?????????????
        self.__color = color
        self.filled = False

    def get_color(self):        # геттер v
        return self.__color

    def set_color(self, r, g, b):       # сеттер v
        if self.__isvalid_color(r, g, b):
            self.__color = [r, g, b]


    def get_sides(self):        # геттер v
        return self.__sides

    def set_sides(self, *sides):        # сеттер v
        if self.__isvalid_sides(*sides):
            self.__sides = sides

    def  __is_valid_color(self, r, g, b):
        for i in r, g, b:
            if not 0 < i < 256:
                print('Недопустимый цвет')
            else: self.i = i

    def  __is_valid_sides(self, *sides):            # переделать по строкам V
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self):
        return sum(self.__sides)







class Circle:
    sides_count = 1
    def __init__(self, color, sides):
        super().__init__(color, sides)
        if self.__isvalid_sides(*sides):
            self.__sides = sides
        else:
            [1] * self.sides_count
        self.__radius = self.__sides / (math.pi * 2)

    def __is_valid_sides(self, *sides):
        return len(sides) >= self.sides_count and all(isinstance(sides[0], int) and sides[0] > 0 )  #???????????

    def get_square(self):
        return self.__radius ** 2 * math.pi

    pass
class Triangle:
    sides_count = 3
    pass
class Cube:
    sides_count = 12
    pass