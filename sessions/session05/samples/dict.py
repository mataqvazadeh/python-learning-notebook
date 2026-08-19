my_info = {
    'first-name': 'Mohammad Ali',
    'education':{
        'diplma': 'math',
        'bs': 'cs',
        'ms': 'cs',
    },
    'companies': [
        'pishrobot',
        'system group',
        'nobitex',
    ],
}

products = [
    {
        'name': 'ball',
        'color': 'red',
        'size': {
            'radius': 5,
        },
    },
    {
        'name': 'book',
        'size': {
            'width': 10,
            'length': 20,
        },
        'pages': 100,
    },
]

# print(products)
# print('=' * 50)
# print(products[1])
# print('=' * 50)
# print(products[1]['size'])
# print('=' * 50)
# print(products[1]['size']['width'])
from copy import deepcopy

a = deepcopy(products[0])
print(products[0])
print('=' * 50)
print(f'copy:{a}')

print('=' * 50)
print('=' * 50)

a['size']['radius'] *= 10
print(products[0])
print('=' * 50)
print(f'copy:{a}')
