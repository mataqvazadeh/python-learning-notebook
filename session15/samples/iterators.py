def even_generator(n: int):
    for i in range(1,n+1):
        if i % 2 == 0:
            yield i

# eg = even_generator(10)
# print(next(eg))
# print(next(eg))

class Even:
    def __init__(self, n: int):
        self.max = n

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 2

        if self.counter >= self.max:
            raise StopIteration

        return self.counter        