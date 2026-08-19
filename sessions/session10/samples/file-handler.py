class FileHandler:
    def __init__(self, path:str):
        self.file = open(path, mode='a+')

    def write_my_name(self, name):
        self.file.write(f'YOUR NAME = {name}\n')

    def __del__(self):
        self.file.close()

file_handler = FileHandler('names.txt')
file_handler.write_my_name('Ali')
file_handler.write_my_name('Reza')

file_handler2 = FileHandler('another_names.txt')
file_handler2.write_my_name('Aynaz')
file_handler2.write_my_name('Mohamamd')
file_handler2.write_my_name('Iliya')
