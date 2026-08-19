class LifeCycle:
    def __init__(self):
        print('I initialized ...')

    def __del__(self):
        print('I deleted ...')

def foo():
    a = LifeCycle()
    return a

# a = LifeCycle()
# b = a
# c = [a,b]
# print('del a')
# del a
# print('del b')
# del b

# print('del c[0]')
# del c[0]
# input('enter any key to finish')

print('Before Foo')
b = foo()
print('After Foo')
input('enter any key to finish')
