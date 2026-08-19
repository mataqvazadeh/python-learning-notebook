# fibonacci: 0,1,1,2,3,5,8,13,21,...
# fibo(n) = fibo(n-1) + fibo(n-2)

def fibo(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

#print(fibo(6)) #8
# result = list(map(fibo, range(0,11)))
# print(result)

# factorial: 3! = 3 * 2 * 1
# factorial(n) = n * factorial(n - 1)

def fact(n:int) -> int:
    assert n >= 0, 'n should be positive'
    
    if n <= 1:
        return 1
    
    return n * fact(n - 1)

try:
    print(fact(-1))
except AssertionError as e:
    print(e)

print({f'{i}!': fact(i) for i in range(0, 11)})