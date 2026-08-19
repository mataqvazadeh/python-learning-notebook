class Person:
    def __init__(self, birth_year: int):
        self.birth_year = birth_year

    @property
    def age(self):
        return 1404 - self.birth_year
    
mat = Person(1368)
print(mat.age)