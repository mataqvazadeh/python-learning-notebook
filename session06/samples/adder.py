def adder_2(x: int) -> int:
    return x + 2

def adder_3(x: int) -> int:
    return x + 3

adder_2(10)
adder_3(12)


def make_adder(num:int):
    
    def adder(x: int) -> int:
        return x + num
    
    return adder

def make_adder_2(num:int):
    return lambda x: x + num

adder_5 = make_adder(5)
print(type(adder_5))
print(adder_5(10))

adder_6 = make_adder_2(6)
print(type(adder_6))
print(adder_6(10))

print(make_adder(100)(20))