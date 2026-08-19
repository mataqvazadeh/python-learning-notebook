import abc
class Flyable(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

class Bird(Flyable):
    pass

class Airplane(Flyable):
    pass

# Abstract Class, Interface
class Shape(abc.ABC):
    def __init__(self, color):
        self.color = color

    @abc.abstractmethod
    def get_area(self):
        pass
    
    @abc.abstractmethod
    def get_perimeter(self):
        pass

    def get_color(self):
        return self.color

class Rectangle(Shape):
    def __init__(self, w, L, color):
        super().__init__(color)
        self.width = w
        self.length = L

    def get_area(self):
        return self.width * self.length
    
    def get_perimeter(self):
        return 2 * (self.width + self.length)
    
import math
class Circle(Shape):
    def __init__(self, r, color):
        super().__init__(color)
        self.radius = r

    def get_area(self):
        return (self.radius ** 2) * math.pi
    
    def get_perimeter(self):
        return 2 * self.radius * math.pi

class Triangle(Shape):
    def __init__(self, h, w, color):
        super().__init__(color)
        self.width = w
        self.height = h
    
    def get_area(self):
        return self.width * self.height / 2
    
    def get_perimeter(self):
        return 20

def area_calculator(sh:Shape) -> float:
    return sh.get_area()

def main():
    a = Rectangle(10, 30, 'red')
    print(area_calculator(a))
    print(a.get_color())

    t = Triangle(10, 5, 'blue')
    print(area_calculator(t))
    print(t.get_color())
    # sh = Shape()
    # print(sh.get_area())
    # print(sh.get_perimeter())

if __name__=='__main__':
    main()



