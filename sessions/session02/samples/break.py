numbers = []
for i in range(1, 11):
    numbers.append(i)

print(numbers)

for number in numbers:
    if number % 2 == 1:
        continue
    print(number)

for number in numbers:
    if number > 5:
        break
    print(number)

if 1 < 2:
    continue