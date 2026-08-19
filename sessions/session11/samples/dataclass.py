from dataclasses import dataclass

@dataclass
class Student:
    name :str
    age: int
    sid: str

def print_std(std : Student):
    pass

# enum

class Car:
    def __init__(self):
        self.name = ''