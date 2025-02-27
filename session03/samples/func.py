def print_helloworld():
    print('Hello World!')

def greeting(name):
    print(f'Hellllllllllllo {name}')

def greeting_with_age(age, name):
    print(f'Hello {name}. You are {age} years old!')

def new_greeting(name):
    pass

def greeting_smart(val1, val2):
    if type(val1) is int:
        greeting_with_age(name=val2, age=val1)
    else:
        greeting_with_age(name=val1, age=val2)

# def greeting_list(*names):
#     print(type(names))
#     for name in names:
#         print(f'Hello {name}')

# greeting_list('emad')
# print('=' * 20)
# greeting_list('emad', 'amir')
# print('=' * 20)
# greeting_list('emad', 'razieh', 'mina')
# print('=' * 20)
# greeting_list('emad', 'razieh', 'mina', 'maryam')

def foo(**ghazanfar):
    print(type(ghazanfar))
    for key, value in ghazanfar.items():
        print(f'{key} = {value}')

foo(name='emad')
print('=' * 20)
foo(age=12, name='behrooz')
print('=' * 20)
foo(Min=0, Max=22, Average=11)


def my_func(val1, val2, val3=1, val4=2, *args, **kwargs):
    pass


# greeting_smart('mandana', 28)

# print_helloworld()
# greeting('ali')
# greeting('Ali')
# greeting('Reza')
# greeting('Maryam')
# new_greeting('sfdsdf')

# greeting_with_age('maryam', 24)
# greeting_with_age(name='maryam', 'mina', age=24)
# greeting_with_age(age=24, name='maryam')

# greeting_list(['emad', 'amir', 'mina'])

