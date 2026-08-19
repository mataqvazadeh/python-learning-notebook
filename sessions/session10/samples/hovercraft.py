class CarFather:
    def say_something(self):
        print('I am Car Father')

class Car(CarFather):
    def move(self):
        print('Running')

    def get_wheels(self):
        return 4

class BoatFather:
    pass

class Boat(BoatFather):
    def move(self):
        print('Floating')

    def get_paddles(self):
        return 2

class HoverCraft(Car, Boat):
    def __init__(self):
        self.in_water = True

    def get_wheels(self):
        return 0
    
    def move(self):
        if self.in_water:
            return Boat.move(self)
        else:
            return Car.move(self)


# print('CAR')
# c = Car()
# c.move()
# print(c.get_wheels())

# print('BOAT')
# b = Boat()
# b.move()
# print(b.get_paddles())

print('HOVER CRAFT')
print(HoverCraft.mro())
hc = HoverCraft()
print(hc.get_paddles())
print(hc.get_wheels())
hc.say_something()
hc.move()
hc.in_water = False
hc.move()
hc.in_water = True
hc.move()