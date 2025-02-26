user_input = input('Enter a list of integers, separate them with white space: ')

numbers_str = user_input.split()

numbers = []
for num_str in numbers_str:
    num = int(num_str)
    numbers.append(num)

print('Numbers = [', end='')
for index, number in enumerate(numbers):
    if index == (len(numbers) - 1):
        print(number,end=']\n')
    else:
        print(number, end=',')