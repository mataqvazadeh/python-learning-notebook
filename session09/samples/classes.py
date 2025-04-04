class MyClass:
    pass

a = MyClass()
b = MyClass()

class Car:
    wheels = 4
    counter = 0

    def __init__(self, color: str, model: str,masraf:float):
        self.gas_tank = 0
        self.color = color
        self.model = model
        self.masraf = masraf
        Car.counter += 1

    def beep(self):
        print('Beeeeep!')

    def move(self, km :int):
        self.gas_tank -= self.gas_usage_calculator(km, self.masraf)
        print(f'{self.color} {self.model} moved {km} kilometers')
        self.show_gas()
        self.show_counter()
        self.convert_kmh_to_ms(60)

    def fill_gas(self, gas_in_litter: float):
        self.gas_tank += gas_in_litter
        print(f'{self.color} {self.model} filled by {gas_in_litter} litters')

    def show_gas(self):
        print(f'{self.color} {self.model} has {self.gas_tank} litters of gas')

    @classmethod
    def show_counter(cls):
        print(f'We have {cls.counter} cars totally.')

    @staticmethod
    def convert_kmh_to_ms(kmh:float) -> float:
        return kmh / 3.6
    
    @staticmethod
    def gas_usage_calculator(km: float, masraf: float) -> float:
        return (km / 100) * masraf


print(f'Car Wheels = {Car.wheels}')
# ERROR: print(Car.color)
# object, instance
#print(f'Car Counter = {Car.counter}')
Car.show_counter()
bmw = Car(model='bmw', color='blue', masraf=5)
#print(f'Car Counter = {Car.counter}')
Car.show_counter()
# print(type(bmw))
# bmw.beep()
# #Car.beep(bmw)
# bmw.move(100)
# #Car.move(bmw, 100)

# bmw.fill_gas(10)
bmw.show_gas()
bmw.move(52)
# bmw.show_gas()
# print(bmw.wheels)

print('*' * 50)

pride = Car('White', 'Pride', 7)
#print(f'Car Counter = {Car.counter}')
Car.show_counter()
# pride.fill_gas(10)
pride.show_gas()
# pride.move(52)
# pride.show_gas()
# bmw.show_gas()

# print(pride.wheels)

# Car.wheels = 3
# print(pride.wheels)
# print(bmw.wheels)

# Car.wheels = 2
# print(pride.wheels)
print('*' * 50)

a = Car('black', 'jack', 8)
#print(f'Car Counter = {Car.counter}')
Car.show_counter()
a.show_gas()

print('*' * 50)
res = Car.convert_kmh_to_ms(60)
print(f'60 km/h = {res} m/s')