import math

class Figure:
    r, g, b = 0, 0, 0           # черный
    sides_count = 0
    __color = [r, g, b]

    def __init__(self, color, *sides):
        self.__color = color
        self.__sides = sides
        self.filled = False

    def get_color(self):
        # self.set_color(self, self.__color)# геттер v
        return self.__color

    def  __is_valid_color(self, r, g, b):
        color_ = [r, g, b]
        for i in color_:
            self.colored = all(isinstance(i, int) and (0 <= i < 256) for i in color_)
        return self.colored

    def set_color(self, r, g, b):       # сеттер v
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        return self.__color


    def get_sides(self):        # геттер v
        return list(self.__sides)

    def set_sides(self, *new_sides):        # сеттер v
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def  __is_valid_sides(self, *sides):            # проверили V
        return len(sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self):
        return sum(self.__sides)




class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count
        self.filled = False
        self.__radius = self.__sides[0] / (math.pi * 2)
    def __is_valid_sides(self, *sides):
        for i in sides:
            return isinstance(i, int) and i > 0 and len(sides) == self.sides_count
    def get_square(self):
        return f'Площадь круга: {self.__radius ** 2 * math.pi}'


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        try:
            if self.__is_valid_sides(*sides):
                self.__sides = sides
                self.p = sum(self.__sides) / 2
                self.s = math.sqrt(self.p * (self.p - self.__sides[0]) * (self.p - self.__sides[1])
                                   * (self.p - self.__sides[2]))
                self.footing = max(self.__sides)
                self.__height = 2 * self.s / self.footing
            else:
                self.__sides = [1] * self.sides_count
        except TypeError:
            print('Недопустимый формат длины сторон')
        self.filled = False
    def __is_valid_sides(self, *sides):
        for i in sides:
            return isinstance(i, int) and i > 0 and len(sides) == self.sides_count

    def get_square(self):
        return f'Площадь треугольника = {self.s}'


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if self.__is_valid_sides(*sides):
                                                                        # !!!!!!!!!!!!!!!!!!!!!!!!
            self.__sides = [sides[0]] * self.sides_count

            print(f'self.__sides of cube {self.__sides}')
                                                                        #!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            self.__sides = [1] * self.sides_count
    def __is_valid_sides(self, *sides):
        for i in sides:
            return isinstance(i, int) and i > 0 and len(sides) == 1
    def get_volume(self, *sides):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
cube1.set_sides(18)
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


# circle1 = Circle((200, 200, 100), 17, 18)
# circle2 = Circle((100, 100, 200), 35)
# circle1.set_sides(33) # Изменится
# print(f'circle1.get_sides() {circle1.get_sides()}')
# print(f'длина окружности {len(circle1)}')
# print(circle1.get_square())
# print(f'Radius = {circle1._Circle__radius}')
#
# triangle1 = Triangle((200, 200, 100), 15, 17, 18)
# triangle2 = Triangle((200, 200, 100), 15, 17)
#
# cube1 = Cube((200, 200, 100), 6)
# print(cube1.get_volume())
# cube2 = Cube((200, 200, 100), 4, 6)