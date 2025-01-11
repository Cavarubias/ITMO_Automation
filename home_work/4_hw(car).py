class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def year_of_production(self):
        print(f'Год выпуска - {self.year}')

    def type_of_car(self):
        print(f'Тип - {self.type}')

    def color_of_car(self):
        print(f'Цвет - {self.color}')


attributes = Car('Черный', 'Кроссовер', '2015')
attributes.start()
attributes.stop()
attributes.year_of_production()
attributes.type_of_car()
attributes.color_of_car()