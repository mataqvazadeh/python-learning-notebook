class Animal:
    animals_count = 0

    def __init__(self, name: str, foods: list, species:str):
        self.name = name
        self.foods = foods
        self.species = species
        Animal.animals_count += 1

    def eat(self, food: str):
        if food in self.foods:
            print('I ate {}.'.format(food))
        else:
            print('I hate {}.'.format(food))

    def say_something(self):
        print(f'I am a {self.species}')
        print(f'My name is {self.name}')

    def move(self):
        print('I am walking.')

dog = Animal(name='puppy', species='Dog', foods=['Bone','Meat'])
print(f'{' Dog ':*^15}')
print(Animal.animals_count)
print(f'Is Animal? {isinstance(dog, Animal)}')
print(f'Is Float? {isinstance(dog, float)}')
cow = Animal(name='browny', species='Cow', foods=['Grass', 'Corn', 'Straw'])
print(f'\n{' Cow ':*^15}')
print(Animal.animals_count)
print(f'Is Animal? {isinstance(cow, Animal)}')

# dog.say_something()
# dog.eat('Bone')
# dog.eat('Grass')
# dog.move()

# cow.say_something()
# cow.eat('Bone')
# cow.eat('Grass')
# cow.move()

duck = Animal(name='donald', species='Duck', foods=['Grass'])
print(f'\n{' Duck ':*^15}')
print(Animal.animals_count)
print(f'Is Animal? {isinstance(duck, Animal)}')
duck.say_something()
duck.eat('Bone')
duck.eat('Grass')
duck.move()

class Duck(Animal):
    def __init__(self, name):
        super().__init__(name=name, foods=['Grass'], species='Duck')

    def say_something(self):
        # super().say_something()
        print('Quaaaak')

    def move(self):
        print('Swimming ...')

duck2 = Duck(name='ducky')
print(f'\n{' Duck 2 ':*^15}')
print(Animal.animals_count)
print(type(duck2))
print(f'Is Animal? {isinstance(duck2, Animal)}')
print(f'Is Duck? {isinstance(duck2, Duck)}')
duck2.say_something()
duck2.eat('Bone')
duck2.eat('Grass')
duck2.move()

print('-' * 15)
print(f'Is Animal subclass of Duck: {issubclass(Animal, Duck)}')
print(f'Is Animal subclass of float: {issubclass(Animal, float)}')
print(f'Is Animal subclass of str: {issubclass(Animal, str)}')
print(f'Is Duck subclass of Animal: {issubclass(Duck, Animal)}')
print(f'Is Duck subclass of str: {issubclass(Duck, str)}')

class SubDuck(Duck):
    pass
print('-' * 15)

print(f'Is Duck subclass of Animal: {issubclass(Duck, Animal)}')
print(f'Is SubDuck subclass of Duck: {issubclass(SubDuck, Duck)}')
print(f'Is SubDuck subclass of Animal: {issubclass(SubDuck, Animal)}')


class Dog(Animal):
    pass
print('-' * 15)

print(f'Is Dog subclass of Animal: {issubclass(Dog, Animal)}')
print(f'Is Dog subclass of Duck: {issubclass(Dog, Duck)}')

b = Dog('goofy', [''], 'Dog')
print(f'Is Duck? {isinstance(b, Duck)}')

