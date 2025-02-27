def print_list(lst, message, sep=', ', end='\n'):
    print(f'{message} = {{', end='')
    for index, element in enumerate(lst):
        if index == (len(lst) - 1):
            print(element,end=f'}}{end}')
        else:
            print(element, end=sep)


user_input = input('Enter a list of integers, separate them with white space: ')

numbers_str = user_input.split()

numbers = []
for num_str in numbers_str:
    num = int(num_str)
    numbers.append(num)

print_list(numbers, 'Numbers', end='\n\n')

even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print_list(odd, 'Odd Numbers', '*')
print_list(even, 'Even Numbers', '-')