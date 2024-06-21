class Vehicle:
    __COLOR_VARIANTS = ['BLACK', 'WHITE', 'YELLOW', 'PINK', 'BLUE']
    def __init__(self, owner, model, color, engine_power):
        self.owner = 'Ivan'
        self.__model = 'Toyota RAV 4'
        self.__engine_power = 160
        self.__color = 'white'

        """
            Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color; 
    а так же владельца в конце в формате "Владелец: <имя>"
    Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, 
    если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>"."""

    def get_model(self):
        return f'Модель: {self.model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.engine_power}'

    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(f'{Vehicle.get_model(self)}\n{Vehicle.get_horsepower(self)}\n{Vehicle.get_color(self)}\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.upper() in Vehicle.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")





class Sedan(Vehicle):
    def __init__(self, owner, model, color, engine_power):
        self.__PASSENGERS_LIMIT = 5
        self.owner = owner
        self.model = model
        self.color = color
        self.engine_power = engine_power


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.get_model()
vehicle1.print_info()

vehicle1.set_color('GREEN')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'

vehicle1.print_info()