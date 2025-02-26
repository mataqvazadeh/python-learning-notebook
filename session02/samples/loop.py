print('*' * 5, 'Hope by for', '*' * 5)
for number in range(1, 21):
    if number % 5 == 0:
        print('Hope')
    else:
        print(number)

print('*' * 5, 'Hope by while', '*' * 5)
number = 1
while number < 21:
    if number % 5 == 0:
        print('Hope')
    else:
        print(number)
    number += 1
