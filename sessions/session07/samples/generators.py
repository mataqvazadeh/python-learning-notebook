def simple_generator():
    yield 1
    yield 2
    yield 3

result = simple_generator()
# print(type(result))
# print(result)
# print('=' * 10)

# # for n in result:
# #     print(n)

# print('=' * 10)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# print(next(result))

def factorial_generator(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result

def my_map(function, iterable):
    for element in iterable:
        result = function(element)
        yield result

def my_count(start = 0, step = 1):
    while True:
        yield start
        start += step