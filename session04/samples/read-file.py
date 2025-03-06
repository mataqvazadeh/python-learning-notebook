# f = open('text01.txt', mode='r')
# s = f.read()
# print(type(s))
# print(s)
# print(s)
# print('-'*50)
# print(f.read(5))
# print('-'*50)

# print(f.read())
# print('-'*50)
# print(f.read())
# print('-'*50)
# print(f.tell())
# print(f.seek(0))
# print('-'*50)
# print(f.read())
# for line in f:
#     print(line)
#     print('*'*10)

# f = open('text01.txt', mode='r')

# L = f.readline()
# print(L)
# print('-'*50)
# print(f.read(5))
# print('-'*50)
# print(f.readline())

# f.seek(0)

# lines = f.readlines()
# print(lines)
# print(lines[0])

# f.close()

# with open('text02.txt', mode='r') as file:
#     print(file.read())
#     file.seek(0)

# print('-'*50)
# print(file.read())

not_found_file = open('text_root.txt', mode='r')
print(not_found_file.read())