def two_number_operation(a: int, b: int, op) -> int:
    result = op(a,b)
    return result

def add(a,b):
    return a + b

def minus(a,b):
    return a - b

# print(f'add 1 to 2: {two_number_operation(1,2,add)}')
# print('*' * 50)
# print(f'minus 2 from 1: {two_number_operation(1,2,minus)}')
print(f'5 multiply by 5: {two_number_operation(5,5,lambda x, y: [x + y, x - y])}')

def is_even(a:int) -> bool:
    return a % 2 == 0

lst = list(range(1,11))

# print(lst)
# print('*' * 50)
# # result = list(map(is_even, lst))
# result = list(map(lambda number: number % 2 == 0, lst))
# print(result)

# print(lst)
# print('*' * 50)
# # result = list(filter(is_even, lst))
# result = list(filter(lambda number: number % 3 == 0, lst))
# print(result)

# from functools import reduce

# print(lst)
# print('*' * 50)
# # # total = reduce(add, lst, 100)
# # total = reduce(lambda x, y : x * y, lst)
# # print(total)
# # print('*' * 50)
# # minuses = reduce(minus, lst, 100)
# # print(minuses)

# lst = ['reza', 'mohammad', 'ali', 'sina']
# print(lst)
# print('*' * 50)
# result = sorted(lst)
# print(result)

# # def sort_by_len(s: str):
# #     return len(s)

# # result = sorted(lst,key=sort_by_len)
# result = sorted(lst,key=len)
# print('*' * 50)
# print(result)

