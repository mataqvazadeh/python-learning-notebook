year = int(input('Enter your birth year: '))
age = 1404 - year

name = input('Enter your name: ')

if not age > 60:
    print('Your are young')
else:
    if 'a' in name:
        print('Hey old man, you have a')
    elif 'b' in name:
        print('Wow')
    else:
        print('You are old')

