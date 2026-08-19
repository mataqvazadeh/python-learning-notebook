# def foo(positional1, positional2, /, pos_name1, pos_name2, *, name1, name2):
#     pass


# foo(1, 2, pos_name1=1, pos_name2=2, name1=1, name2=2)

def bar(name: str, age: int) -> None:
    print(f'age = {age} name = {name}')


# bar('ali', 31)
# bar(31, 'ali')

def sum_two_integer(a1: int, a2: int) -> int:
    return a1 + a2

print(sum_two_integer(1, 2))
print(sum_two_integer('Hello,', 'World'))