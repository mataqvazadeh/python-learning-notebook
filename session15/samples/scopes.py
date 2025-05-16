# Local
# Enclosed
# Global
# Build-in
# LEGB



# Global
x = 12

print(x)

def func1():
    # Enclosed
    #x = 15
    print(x)

    def func2():
        # Local
        # x = 20
        #nonlocal x
        x += 1
        print(x)

        # def func3():
        #     # Local
        #     #x = 25
        #     #global x
        #     print(x)

        # func3()
    func2()

func1()

print(x)
