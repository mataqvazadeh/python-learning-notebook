import time

def new_function_with_time_calculator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Actual Time: {(time.time() - start) * 1000000}')
        return result

    return wrapper

def logger(msg: str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('=' * 30)
            print(f'|{msg:^28}|')
            print('=' * 30)
            print(f'|{func.__name__:^28}|')
            print('=' * 30)
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator

@new_function_with_time_calculator    
def fibo_rec(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_rec(n-1) + fibo_rec(n-2)

@new_function_with_time_calculator    
def fibo_loop(n: int) -> int:
    if 0 <= n <= 1:
        return n
    
    # 0, 1, 1, 2
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

@new_function_with_time_calculator
@logger('It will add two number')
def add(a,b):
    return a+b

@logger('This is my greeting method')
def greeting():
    print('Hello')

def main():
    # n = int(input('Enter? '))
    # n = 35
    
    # print(fibo_loop(n))
    # print(add(b=10, a=20))

    # greeting()

    print(add(1,2))

if __name__ == '__main__':
    main()
