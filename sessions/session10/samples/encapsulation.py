class MyClass:
    def __init__(self):
        self._num = 0

    @property
    def num(self):
        return self._num * 10

    @num.setter
    def num(self, num):
        if num < 0:
            self._num = 0
        else:
            self._num = num

        

    
a = MyClass()
a.num = -1
print(a.num)
a.num = 10
print(a.num)
a._num = -1
print(a.num)