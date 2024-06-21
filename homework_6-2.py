class Vehicle:
    __COLOR_VARIANTS = ['BLACK', 'WHITE', 'YELLOW', 'PINK', 'BLUE']
    def __init__(self, owner, model, color, engine_power):
        self.owner = 'Ivan'
        self.__model = 'Toyota RAV 4'
        self.__engine_power = 160
        self.__color = 'white'

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
