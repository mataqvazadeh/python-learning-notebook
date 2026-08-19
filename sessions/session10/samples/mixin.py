class DictionarySerializerMixin:
    def to_dict(self) -> dict:
        # return { key.upper() : value for key,value in self.__dict__.items() if key.upper() != 'NAME'}
        return self.__dict__

# JSON = Java Script Object Notation
import json
class JsonSerializerMixin:
    def to_json(self) -> str:
        simple_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, int):
                simple_dict[key] = value
            elif isinstance(value, str):
                simple_dict[key] = value
            elif isinstance(value, float):
                simple_dict[key] = value
            elif isinstance(value, bool):
                simple_dict[key] = value
            else:
                simple_dict[key] = value.__dict__
        # simple_dict = self.__dict__

        return json.dumps(simple_dict)

class LoggerMixin:
    file_path: str = None

    def log(self, message, type):
        import datetime
        message = f'#{type.upper()}# {datetime.datetime.now()} - {message}'        
        if self.file_path:
            with open(self.file_path, mode='a') as file:
                file.write(message)
                file.write('\n')
        else:
            print(message)

    def info(self, message):
        return self.log(message, 'info')

    def debug(self, message):
        return self.log(message, 'debug')

class Employee(DictionarySerializerMixin, JsonSerializerMixin, LoggerMixin):

    def __init__(self, name, age, job_title):
        self.name = name
        self.age = age
        self.job = job_title
        self.info('An Employee Created.')

class Color:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b

class Car(DictionarySerializerMixin, JsonSerializerMixin):
    def __init__(self, model, color: 'Color'):
        self.model = model
        self.color = color

class Cat(DictionarySerializerMixin, LoggerMixin):
    file_path = 'cat-log.txt'
    def __init__(self, name):
        self.name = name

    def get_sound(self):
        print('Miuuuu')
        self.debug('One person called get_sound')

def main():
    print('\nEmployee')
    e = Employee('Reza', 30, 'Developer')
    # print(e.to_dict())
    # print(e.to_json())
    
    print('\nCar')
    c = Car('pride', Color(0,0,0))
    print(c.to_dict())
    print(c.to_json())

    print('\nCat')
    cat = Cat('kitty')
    cat.get_sound()
    # print(cat.to_dict())

if __name__ == '__main__':
    main()