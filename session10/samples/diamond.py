class A:
    def foo(self):
        print('I am A')

class B(A):
    pass

class C(A):
    def foo(self):
        print('I am C')

class D(B,C):
    pass

print(D.mro())
d = D()
d.foo()