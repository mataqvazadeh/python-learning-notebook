def get_integer():
    user_input = input('Enter an integer: ')

    if not user_input.isdigit():
        raise ValueError(f'Your input is not an integer: {user_input}')

def main():
    try:
        get_integer()
    except ValueError as exp:
        print(exp)
        raise FileNotFoundError from None

def main2():
    try:
        main()
    except ValueError:
        print('It was VALUE ERROR')
    except FileNotFoundError:
        print('It was FileNotFoundError')

main2()