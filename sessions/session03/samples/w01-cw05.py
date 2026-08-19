"""
    fjkshdfkjhsfkjhkjfhsdkfjhskdfjsdfkhfs
"""
from random import randint

rand_number = randint(1, 20)

while True:
    user_guess = int(input('Guess an integer between 1 and 20: '))

    if user_guess > rand_number:
        print('Too hight! Try Again!')
    elif user_guess < rand_number:
        print('Too low! Try Again!')
    else:
        print('Correct!')
        break