numbers = [1, 2, 4, 5, 6]

for number in numbers:
    print(number)

print('*' * 20)

iterator = iter(numbers)
while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break
