class MyClass:
    pass

a = MyClass()
b = MyClass()

class Car:
    def beep(self):
        print('Beeeeep!')

    def move(self, km):
        print(f'I move {km} kilometers')

bmw = Car()
print(type(bmw))
bmw.beep()
bmw.move(100)
bmw.beep()
bmw.move(52)