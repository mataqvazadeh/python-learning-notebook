def my_min(*numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum

# a = my_min(1)
# print(a)

# print(my_min(1, -1))

# b = my_min(1, 2, 0, 10, -1)
# b = b * 10
# print(b)

def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
    
# print(is_odd(1))
# print(is_odd(2))

def divider(a, b):
    quotient = a // b
    remainder = a % b

    return quotient, remainder

result = divider(5 , 2)
print(result)