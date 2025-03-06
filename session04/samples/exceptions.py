try:
    a = int(input('first number? '))
    b = int(input('second number? '))

    print(a/b)

    # f = open('nothin')
except ZeroDivisionError:
    print('ERROR: Not a Number')
    raise
except  ValueError as exp:
    print('ERROR: Not an Integer')
    print(exp)
except Exception:
    pass
else:
    print('ELSE: Every thing is ok')
finally:
    print('FINALLY: IT is always printed')

# print('program finished')