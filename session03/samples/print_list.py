import list_printer

def main():
    user_input = input('Enter a list of integers, separate them with white space: ')

    numbers_str = user_input.split()

    numbers = []
    for num_str in numbers_str:
        num = int(num_str)
        numbers.append(num)

    list_printer.print_pretty(numbers, 'Numbers', end='\n\n')

    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    list_printer.print_pretty(odd, 'Odd Numbers', '*')
    list_printer.print_stupid(even)

if __name__ == '__main__':
    main()